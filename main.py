import pygame as pg
from math import cos, sin, radians
from Components import Window, Edge, Vert
pg.init()


class Cube:
    def __init__(self, dimensions, total_z_offset, win_dim: tuple):
        self.c_window = None
        self.screen = None
        self.win_dim = win_dim
        self.dimensions = dimensions
        self.total_z_offset = total_z_offset  # the z-distance between the two main faces
        assert (self.dimensions >= 40)  # 30 min size
        self.f_plane = []  # front
        self.b_plane = []  # back
        self.l_plane = []
        self.r_plane = []
        self.t_plane = []
        self.bt_plane = []
        self.cube_planes = None
        self.init_vert_s()
        assert (len(self.f_plane) > 1 and len(self.b_plane) > 1)
        self.vert_s = [self.f_plane, self.b_plane]
        self.edges = None
        self.init_edges()
        self.t_dis_y = 0
        self.f_count = 0
        assert (self.edges is not None and len(self.edges) > 1)

    def init_vert_s(self):
        p_part = self.dimensions // 2  # the placement of the vertices based from the size of the cube
        _off = self.win_dim[0] // 2
        z_o = self.total_z_offset
        self.f_plane = [
            Vert(x=p_part,
                 y=p_part,
                 z=0),  # top right front
            Vert(x=p_part,
                 y=(-p_part),
                 z=0),
            Vert(x=(-p_part),
                 y=(-p_part),
                 z=0),
            Vert(x=(-p_part),
                 y=p_part,
                 z=0)
        ]
        self.b_plane = [Vert(x=(point.original_x // z_o),
                             y=(point.original_y // z_o),
                             z=2) for point in self.f_plane]

        self.r_plane = [
            self.f_plane[0],  self.f_plane[1], self.b_plane[1], self.b_plane[0],
        ]
        self.l_plane = [
            self.f_plane[2], self.f_plane[3], self.b_plane[3], self.b_plane[2]
        ]
        self.t_plane = [
            self.f_plane[0], self.f_plane[3], self.b_plane[3], self.b_plane[0]
        ]
        self.bt_plane = [
            self.f_plane[1], self.f_plane[2], self.b_plane[2], self.b_plane[1]
        ]

    def init_edges(self):
        vert_pool = self.f_plane + self.b_plane
        edge_def = [[0, 1], [1, 2], [2, 3], [3, 0], [4, 5], [5, 6], [6, 7], [7, 4], [0, 4], [1, 5], [2, 6], [3, 7]]
        self.edges = [Edge(point_a=vert_pool[e[0]],
                           point_b=vert_pool[e[1]]
                           ) for e in edge_def]

        assert(self.edges is not None)
        assert(len(self.edges) == 12)

    def rotate_y(self, pitch):

        assert (pitch < 180)
        self.t_dis_y += pitch
        self.f_count += 1

        if self.f_count == 2:
            r = radians(self.t_dis_y)
            for point in self.f_plane + self.b_plane:
                point.c_X = round(point.original_x * cos(r) - point.original_y * sin(r), 5)
                point.c_Y = round(point.original_x * sin(r) + point.original_y * cos(r), 5)
                print("EX reached " + str(point))
            self.f_count = 0
            return

        r = radians(pitch)
        for point in self.f_plane + self.b_plane:
            point.c_X = round(point.c_X * cos(r) - point.c_Y * sin(r), 5)
            point.c_Y = round(point.c_X * sin(r) + point.c_Y * cos(r), 5)
            print(point)

    def render_cube(self):
        # render vertices then edges
        self.render_faces()
        self.render_edges()
        self.render_vertices()

    def render_edges(self):
        _off = self.win_dim[0] // 2
        for e in self.edges:
            e.render_edge(self.screen, _off)

    def render_vertices(self):
        vertices = self.f_plane + self.b_plane
        _off = self.win_dim[0] // 2
        # offset the cube to the centre
        for point in vertices:
            pg.draw.circle(
                self.screen,
                (0, 0, 0),
                (point.c_X + _off, point.c_Y + _off),
                2
            )

    def render_faces(self):

        _off = self.win_dim[0] // 2
        dims = [[fv.c_X + _off, fv.c_Y + _off] for fv in self.b_plane]
        # back face
        pg.draw.polygon(
            self.screen,
            (0, 0, 225),
            dims
        )

        all_edges = [
            self.l_plane,
            self.r_plane,
            self.t_plane,
            self.bt_plane
        ]
        for plane_v in all_edges:
            temp = [[fv.c_X + _off, fv.c_Y + _off] for fv in plane_v]
            pg.draw.polygon(
                self.screen,
                (100, 200, 225),
                temp
            )


window_dim = (700, 700)
cube = Cube(200, 3, window_dim)
sim_window = Window(cube, window_dim)
win = sim_window.get_window()
clock = pg.time.Clock()

while sim_window.is_running:
    clock.tick(100)
    win.fill((225, 225, 225))
    sim_window.handle_events()
    cube.render_cube()
    pg.display.flip()
