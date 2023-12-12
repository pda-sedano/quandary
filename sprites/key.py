from my_base_sprite import MyBaseSprite
import pygame as pg


# Parameters
width = 200
height = 100


class Key(MyBaseSprite):
    """
    A simple key.
    """
    def __init__(self, x, y):
        super().__init__(x, y, width, height, key='key.png')
        self.draw()

    def draw(self):
        self.image.blit(pg.transform.scale(self.key, (width, height)), (0, 0))

    def update(self, event=None):
        if event is not None:
            self.drag(event)
