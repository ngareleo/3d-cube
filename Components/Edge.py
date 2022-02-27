import pygame as pg


class Edge:

    def __init__(self, point_a, point_b):
        self.point_a = point_a
        self.point_b = point_b

    def __repr__(self):
        return f"from {self.point_a} to {self.point_b}"

    def __str__(self):
        return f"from {self.point_a} to {self.point_b}"

    def render_edge(self, screen, _off):
        pg.draw.line(screen, (0, 0, 0),
                     (self.point_a.c_X + _off, self.point_a.c_Y + _off),
                     (self.point_b.c_X + _off, self.point_b.c_Y + _off),
                     2)

