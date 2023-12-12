import os
from pathlib import Path
import pygame as pg


class MyBaseSprite(pg.sprite.Sprite):
    """
    Base class for a sprite that loads all images necessary for
    it. The kwargs should be a list of names like attr_name='path'
    """
    def __init__(self, x, y, width, height, base_path='../sprite_data', **kwargs):
        super().__init__()
        self.image = pg.Surface((width, height), pg.SRCALPHA)
        self.rect = self.image.get_rect(topleft=(x, y))
        self.base_path = base_path
        self.import_images(**kwargs)
        self.dragging = False
        self.offset_x = 0
        self.offset_y = 0

    # Inspiration from https://stackoverflow.com/a/1389202
    # and https://www.pygame.org/docs/tut/ChimpLineByLine.html
    def import_images(self, **kwargs):
        for key, value in kwargs.items():
            image = pg.image.load(os.path.join(self.base_path, value)).convert_alpha()
            setattr(self, str(Path(key).with_suffix('')), image)

    def drag(self, event):
        if event.type == pg.MOUSEBUTTONDOWN:
            self.dragging = self.rect.collidepoint(event.pos)
            self.offset_x = self.rect.x - event.pos[0]
            self.offset_y = self.rect.y - event.pos[1]
        elif event.type == pg.MOUSEBUTTONUP:
            self.dragging = False

        if self.dragging:
            self.rect.x = pg.mouse.get_pos()[0] + self.offset_x
            self.rect.y = pg.mouse.get_pos()[1] + self.offset_y
