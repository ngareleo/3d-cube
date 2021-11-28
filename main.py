import pygame as pg

pg.init()


class Window:
    def __init__(self):
        self.win_dim = 700
        self.game_window = pg.display.set_mode((self.win_dim, self.win_dim))
        self.is_running = True
        pg.display.set_caption('3d Cube')

    def get_window(self):
        return self.game_window

    def handle_events(self):
        evs = pg.event.get()
        for event in evs:
            if event.type == pg.QUIT:
                self.is_running = False

            elif event.type == pg.K_RIGHT:
                pass

    def get_dim(self):
        return self.win_dim


class Cube:

    def __init__(self, window, dimensions, total_z_offset):
        self.c_window = window
        self.screen = window.get_window()
        self.dimensions = dimensions
        self.total_z_offset = total_z_offset
        assert (self.dimensions >= 40)  # 30 min size
        self.f_plane = []
        self.b_plane = []
        self.init_vert_s()
        assert (len(self.f_plane) > 1 and len(self.b_plane) > 1)
        self.vert_s = [self.f_plane, self.b_plane]
        self.edges = None
        self.init_edges()

        assert (self.edges is not None and len(self.edges) > 1)

    def init_vert_s(self):

        p_part = self.dimensions // 2
        _off = self.c_window.get_dim() // 2
        z_o = self.total_z_offset
        self.f_plane = [
            Vert(x=p_part,
                 y=p_part,
                 z=0),
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
        self.b_plane = [Vert(x=(point.original_x * z_o),
                             y=(point.original_y * z_o),
                             z=2
                             ) for point in self.f_plane]

    def init_edges(self):
        vert_pool = self.f_plane + self.b_plane
        edge_def = [[0, 1], [1, 2], [2, 3], [3, 0], [4, 5], [5, 6], [6, 7], [7, 4], [0, 4], [1, 5], [2, 6], [3, 7]]
        self.edges = [Edge(point_a=vert_pool[e[0]],
                           point_b=vert_pool[e[1]]
                           ) for e in edge_def]
        assert (self.edges is not None)

    def render_cube(self):
        # render vertices then edges
        self.render_edges()
        self.render_vertices()

    def render_edges(self):
        _off = self.c_window.get_dim() // 2
        for e in self.edges:
            e.render_edge(self.screen, _off)

    def render_vertices(self):
        vertices = self.f_plane + self.b_plane
        _off = self.c_window.get_dim() // 2
        # offset the cube to the centre
        for point in vertices:
            pg.draw.circle(
                self.screen,
                (0, 0, 0),
                (point.c_X + _off, point.c_Y + _off),
                2
            )


class Vert:

    def __init__(self, x, y, z):
        self.original_x = x
        self.original_y = y
        self.original_z = z
        self.c_X = self.original_x
        self.c_Y = self.original_y
        self.c_Z = self.original_z

        assert (self.c_X == self.original_x)
        assert (self.c_Y == self.original_y)
        assert (self.c_Z == self.original_z)


class Edge:
    def __init__(self, point_a, point_b):
        self.point_a = point_a
        self.point_b = point_b

    def __repr__(self):
        return f"from {self.point_a} to {self.point_b}"

    def __str__(self):
        return f"from {self.point_a} to {self.point_b}"

    def render_edge(self, screen, _off):
        pg.draw.line(
            screen,
            (0, 0, 0),
            (self.point_a.c_X + _off, self.point_a.c_Y + _off),
            (self.point_b.c_X + _off, self.point_b.c_Y + _off),
            2
        )


sim_window = Window()
win = sim_window.get_window()
cube = Cube(sim_window, 60, 2)

while sim_window.is_running:

    win.fill((225, 225, 225))

    sim_window.handle_events()
    cube.render_cube()
    pg.display.flip()






