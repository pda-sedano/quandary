import sys
import pygame as pg
from sprites.key import Key


# parameters
width, height = 800, 800
fps = 60
black = (0, 0, 0)

pg.init()
window = pg.display.set_mode((width, height))
clock = pg.time.Clock()
key = Key(50, 50)
sprites = pg.sprite.RenderPlain(key)

while True:
    clock.tick(fps)

    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            sys.exit()

        key.update(event)

    window.fill(black)
    sprites.draw(window)
    pg.display.flip()

