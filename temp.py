import pygame as pg

pg.init()
screen = pg.display.set_mode((400, 400))


while True:


    screen.fill((225, 225, 225))
    for event in pg.event.get():

        print(event)
    pg.draw.polygon(
        screen,
        (225, 0, 0),
        ((0, 0), (10, 300), (300, 300), (300, 10))
    )
    pg.display.flip()