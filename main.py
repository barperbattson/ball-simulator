import pygame as pg
import sys

from ball import Ball

# INITIALIZES PYGAME
pg.init()

_SIZE = (500,500)
_WINDOW = pg.display.set_mode(_SIZE)
_CLOCK = pg.time.Clock()

balls_spawned = pg.sprite.Group()

while True:
    balls_spawned.update(_SIZE[0], _SIZE[1])
    _WINDOW.fill((0,0,0))
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            sys.exit()

        if event.type == pg.MOUSEBUTTONDOWN and event.button == 1:
            ball = Ball(_WINDOW, 20, (255,0,0), (_SIZE[0] // 2, _SIZE[1] // 2), (0, 0), 0.5, 0.8, 0.99)
            
            balls_spawned.add(ball)

    balls_spawned.draw(_WINDOW)

    pg.display.flip()
    _CLOCK.tick(60)

if __name__ == "__main__":
    main()