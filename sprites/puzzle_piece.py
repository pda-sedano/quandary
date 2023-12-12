import pygame as pg

from sprites.my_base_sprite import MyBaseSprite

# parameters
original_image_width = 430
original_image_width_version_3 = 522
original_image_height = 337

scale_factor = 100 / original_image_width


color = (255, 215, 0)  # from https://html-color.codes/gold
images = ['blue0.png', 'blue1.png', 'red0.png', 'red1.png']
right_click = 3
snap_length_fraction = 2443 / 8889
width_snap_tolerance = 3
height_snap_tolerance = 3
clear = (0, 0, 0, 0)


class PuzzlePiece(MyBaseSprite):
    """Puzzle piece of one of four different versions denoted by 0, 1, 2, or 3."""
    def __init__(self, version, x, y):
        old_width = original_image_width_version_3 if version == 3 else original_image_width
        width = old_width * scale_factor
        height = width * original_image_height / old_width
        super().__init__(x, y, width, height, picture=images[version])
        self.version = version
        self.orientation = 0
        self.draw()

    def draw(self):
        self.image.fill(clear)
        self.image.blit(pg.transform.scale(self.picture, (self.rect.width, self.rect.height)), (0, 0))

    # TODO: Duplication
    def update(self, event=None):
        if event is not None:
            self.drag(event)

            # flip
            if event.type == pg.MOUSEBUTTONDOWN and event.button == right_click and self.rect.collidepoint(event.pos):
                self.image = pg.transform.flip(self.image, True, False)
                self.orientation = not self.orientation

            # snap
            # extender length = 24.43 mm
            # main square length = 88.89 mm
            # 2443/8889 is in lowest terms
            # We must move one surface forward by 2443/8889 of length

    def snap(self, other):
        # Determines if the snapping is valid (this is the win condition of the CHSH game + orientation constraints
        # + posiiton constraints)
        # TODO: Make this mess a lot clearer
        if ((((self.version % 2) ^ (other.version % 2)) == ((self.version >> 1) & (other.version >> 1)))
                and ((self.version >> 1) == (other.version >> 1) == 1 ^ (self.orientation == other.orientation))
                and ((abs(self.rect.x - other.rect.x - snap_length_fraction * self.rect.width) < width_snap_tolerance)
                     and (abs(self.rect.y - other.rect.y) < height_snap_tolerance))):
            self.rect.x = other.rect.x - snap_length_fraction * self.rect.width
            self.rect.y = other.rect.y
