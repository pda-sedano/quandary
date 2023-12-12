import sys
import pygame as pg
from sprites.chest import Chest, CHEST_OPEN, CHEST_CLOSE

# parameters
width, height = 800, 800
fps = 60
black = (0, 0, 0)

pg.init()
window = pg.display.set_mode((width, height))
clock = pg.time.Clock()
red_chest = Chest('red', 0, 0)
blue_chest = Chest('blue', 400, 0)
sprites = pg.sprite.RenderPlain(red_chest, blue_chest)

while True:
    clock.tick(fps)

    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            sys.exit()
        elif event.type == pg.KEYDOWN:
            pressed = pg.key.get_pressed()
            if pressed[pg.K_1]:
                pg.event.post(pg.event.Event(CHEST_OPEN))
            elif pressed[pg.K_2]:
                pg.event.post(pg.event.Event(CHEST_CLOSE))

        sprites.update(event)

    sprites.update()  # ensure it updates even when

    window.fill(black)
    sprites.draw(window)
    pg.display.flip()
