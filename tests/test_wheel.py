import sys
import pygame as pg
from sprites.wheel import Wheel


# parameters
width, height = 800, 800
fps = 60
black = (0, 0, 0)

pg.init()
window = pg.display.set_mode((width, height))
clock = pg.time.Clock()
wheel = Wheel()
sprites = pg.sprite.RenderPlain(wheel)

while True:
    clock.tick(fps)

    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            sys.exit()

        sprites.update(event)

    sprites.update()

    window.fill(black)
    sprites.draw(window)
    pg.display.flip()
