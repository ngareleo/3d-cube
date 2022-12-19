import pygame as pg


class Window:
    def __init__(self, cube, window_dimensions):
        self.game_window = pg.display.set_mode(window_dimensions)
        self.is_running: bool = True
        self.cube = cube
        self.cube.screen = self.get_window()
        self.cube.c_window = self
        pg.display.set_caption('3d Cube')

    def get_window(self):
        return self.game_window

    def handle_events(self):
        evs = pg.event.get()
        roll_pool = []
        k_pressed = True
        y_key_pressed = False
        for event in evs:
            if event.type == pg.QUIT:
                self.is_running = False
            elif event.type == pg.K_RIGHT:
                pass
            elif event.type == pg.MOUSEWHEEL:
                if y_key_pressed:
                    print("Y PRESSED")
                roll_pool.append(event)
                movement = 0
                pitch = 10 # degrees
                for roll in roll_pool:
                    movement += roll.y
                self.cube.rotate_cube_y(movement * pitch)
                print(f"Number of rolls = {movement}")
            elif event.type == pg.KEYDOWN:
                # y-axis rotation
                if event.unicode == 'y':
                    y_key_pressed = True
            elif event.type == pg.KEYUP:
                if event.unicode == 'y':
                    y_key_pressed = False


