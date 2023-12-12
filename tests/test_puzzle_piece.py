import sys
import pygame as pg
from sprites.puzzle_piece import PuzzlePiece


# parameters
width, height = 800, 800
fps = 60
black = (0, 0, 0)

pg.init()
window = pg.display.set_mode((width, height))
clock = pg.time.Clock()
puzzle_piece_0 = PuzzlePiece(0, 0, 0)
puzzle_piece_1 = PuzzlePiece(1, 400, 0)
puzzle_piece_2 = PuzzlePiece(2, 0, 400)
puzzle_piece_3 = PuzzlePiece(3, 400, 400)
sprites = pg.sprite.RenderPlain(puzzle_piece_0, puzzle_piece_1, puzzle_piece_2, puzzle_piece_3)

while True:
    clock.tick(fps)

    for event in pg.event.get():
        print(f"EVENT TYPE: {event.type}")
        if event.type == pg.MOUSEBUTTONDOWN:
            print(f"event button: {event.button}")
        if event.type == pg.QUIT:
            pg.quit()
            sys.exit()

        sprites.update(event)

    sprites.update()

    window.fill(black)
    sprites.draw(window)
    pg.display.flip()
