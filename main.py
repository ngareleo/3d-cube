import pygame as pg
from math import cos, sin, radians
from components import Window, Edge, Vertex
pg.init()


class Cube:
    def __init__(self, dimensions, depth, window_dimensions: tuple):
        self.c_window = None
        self.screen = None
        self.window_dimensions = window_dimensions
        self.dimensions = dimensions
        self.depth = depth  # the z-distance between the two main faces
        assert (self.dimensions >= 40)  # 30 min size
        self.front_plane = []  # front
        self.back_plane = []  # back
        self.left_plane = []
        self.right_plane = []
        self.top_plane = []
        self.bottom_plane = []
        self.cube_planes = None
        self.initialize_vertices()
        assert (len(self.front_plane) > 1 and len(self.back_plane) > 1)
        self.vert_s = [self.front_plane, self.back_plane]
        self.edges = None
        self.initialize_edges()
        self.t_dis_y = 0
        self.f_count = 0
        assert (self.edges is not None and len(self.edges) > 1)

    def initialize_vertices(self):
        placements = self.dimensions // 2  # the placement of the vertices based from the size of the cube
        _off = self.window_dimensions[0] // 2
        depth = self.depth
        self.front_plane = [
            Vertex(x=placements,
                   y=placements,
                   z=0),  # top right front
            Vertex(x=placements,
                   y=(-placements),
                   z=0),
            Vertex(x=(-placements),
                   y=(-placements),
                   z=0),
            Vertex(x=(-placements),
                   y=placements,
                   z=0)
        ]
        self.back_plane = [Vertex(x=(point.original_x // depth),
                                  y=(point.original_y // depth),
                                  z=2) for point in self.front_plane]

        self.right_plane = [
            self.front_plane[0],  self.front_plane[1], self.back_plane[1], self.back_plane[0],
        ]
        self.left_plane = [
            self.front_plane[2], self.front_plane[3], self.back_plane[3], self.back_plane[2]
        ]
        self.top_plane = [
            self.front_plane[0], self.front_plane[3], self.back_plane[3], self.back_plane[0]
        ]
        self.bottom_plane = [
            self.front_plane[1], self.front_plane[2], self.back_plane[2], self.back_plane[1]
        ]

    def initialize_edges(self):
        vertices_pool = self.front_plane + self.back_plane
        edge_pairings = [[0, 1], [1, 2], [2, 3], [3, 0], [4, 5], [5, 6], [6, 7], [7, 4], [0, 4], [1, 5], [2, 6], [3, 7]]
        self.edges = [Edge(point_a=vertices_pool[edge[0]],
                           point_b=vertices_pool[edge[1]]
                           ) for edge in edge_pairings]

        assert(self.edges is not None)
        assert(len(self.edges) == 12)

    def rotate_cube_y(self, pitch):

        assert (pitch < 180)
        self.t_dis_y += pitch
        self.f_count += 1

        if self.f_count == 2:
            r = radians(self.t_dis_y)
            for point in self.front_plane + self.back_plane:
                point.coordinate_x = round(point.original_x * cos(r) - point.original_y * sin(r), 5)
                point.coordinate_y = round(point.original_x * sin(r) + point.original_y * cos(r), 5)
                print("EX reached " + str(point))
            self.f_count = 0
            return

        r = radians(pitch)
        for point in self.front_plane + self.back_plane:
            point.coordinate_x = round(point.coordinate_x * cos(r) - point.coordinate_y * sin(r), 5)
            point.coordinate_y = round(point.coordinate_x * sin(r) + point.coordinate_y * cos(r), 5)
            print(point)

    def render_cube(self):
        # render vertices then edges
        self.render_faces()
        self.render_edges()
        self.render_vertices()

    def render_edges(self):
        _off = self.window_dimensions[0] // 2
        for e in self.edges:
            e.render_edge(self.screen, _off)

    def render_vertices(self):
        vertices = self.front_plane + self.back_plane
        _off = self.window_dimensions[0] // 2
        # offset the cube to the centre
        for point in vertices:
            pg.draw.circle(
                self.screen,
                (0, 0, 0),
                (point.coordinate_x + _off, point.coordinate_y + _off),
                2
            )

    def render_faces(self):

        _off = self.window_dimensions[0] // 2
        dims = [[vertex.coordinate_x + _off, vertex.coordinate_y + _off] for vertex in self.back_plane]
        # back face
        pg.draw.polygon(
            self.screen,
            (0, 0, 225),
            dims
        )

        edges = [
            self.left_plane,
            self.right_plane,
            self.top_plane,
            self.bottom_plane
        ]
        for plane in edges:
            temp = [[vertex.coordinate_x + _off, vertex.coordinate_y + _off] for vertex in plane]
            pg.draw.polygon(
                self.screen,
                (100, 200, 225),
                temp
            )


window_dimensions = (700, 700)
cube = Cube(200, 3, window_dimensions)
simulation_window = Window(cube, window_dimensions)
window = simulation_window.get_window()
clock = pg.time.Clock()

while simulation_window.is_running:
    clock.tick(100)
    window.fill((225, 225, 225))
    simulation_window.handle_events()
    cube.render_cube()
    pg.display.flip()
