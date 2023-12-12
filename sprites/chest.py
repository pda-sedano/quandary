import pygame as pg
from my_base_sprite import MyBaseSprite


# Params
width = 300
height = 300
fps = 15
clear = (0, 0, 0, 0) # transparent color


# event codes
CHEST_OPEN = pg.USEREVENT + 1
CHEST_CLOSE = pg.USEREVENT + 2


class Chest(MyBaseSprite):
    """
    A treasure chest of color 'red' or 'blue' at the position x, y.
    """
    def __init__(self, color, x, y):
        super().__init__(x, y, width, height, closed='chest_closed.png', opening_1='chest_opening_1.png',
                         opening_2='chest_opening_2.png', opened='chest_open.png',
                         keyhole=f'keyhole_{color}.png')
        self.states = [self.closed, self.opening_1, self.opening_2, self.opened]
        self.state = 0
        self.animation = 0 # 0 indicates no animation, 1 mean opening, -1 means closing
        self.scale_keyhole()
        self.draw()

    def scale_keyhole(self):
        # Resize keyhole
        keyhole_scale_x = self.keyhole.get_size()[0] / self.closed.get_size()[0]
        keyhole_scale_y = self.keyhole.get_size()[1] / self.closed.get_size()[1]
        self.keyhole = pg.transform.scale(self.keyhole, (keyhole_scale_x * width, keyhole_scale_y * height))

    def draw(self):
        chest_image = pg.transform.scale(self.states[self.state], (width, height))
        self.image.blit(chest_image, (0, 0))
        self.image.blit(self.keyhole, (width / 2 - self.keyhole.get_size()[0] / 2,
                                       height / 2 - self.keyhole.get_size()[1] / 2))

    def rotate_keyhole(self, theta):
        self.keyhole = pg.transform.rotate(self.keyhole, theta)

    def update(self, event=None):
        # todo: make sure it's the right chest
        if event is not None:
            if event.type == CHEST_OPEN and self.state == 0:
                self.animation = 1
            elif event.type == CHEST_CLOSE and self.state + 1 == len(self.states):
                self.animation = -1

        if self.animation != 0:
            self.state = self.state + self.animation  # update state
            self.image.fill(clear)
            self.draw()

        if self.state == 0 or self.state + 1 == len(self.states):
            self.animation = 0
