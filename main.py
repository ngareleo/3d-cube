import pygame as pg
from values import *
from itertools import chain
pg.init()
sim_window = pg.display.set_mode(W_SIZE)
pg.display.set_caption(W_CAPTION)
z_offset = 4
plane_a_vertices = [
    [30, 30],  # => a
    [30, -30],  # => b
    [-30, -30],  # => c
    [-30, 30]
]

plane_b_vertices = [[x * z_offset, y * z_offset] for x, y in plane_a_vertices]
cube_def = plane_a_vertices + plane_b_vertices


actual_points = [[vert[0] + (W_SIZE[0]//2), vert[1] + (W_SIZE[1]//2)] for vert in cube_def]
edges = [[0, 1], [1, 2], [2, 3], [3, 0], [4, 5], [5, 6], [6, 7], [7, 4], [0, 4], [1, 5], [2, 6], [3, 7]]

for edge in edges:
    print(f"{cube_def[edge[0]]}, {cube_def[edge[1]]}")

sim_running = True
while sim_running:

    sim_events = pg.event.get()
    sim_window.fill((225, 225, 225))
    for s_event in sim_events:
        if s_event.type == pg.QUIT:
            sim_running = False

    #  draw the points
    for vert in actual_points:
        pg.draw.circle(sim_window, (0, 0, 0), vert, 5)

    # draw the edges
    # front edges

    for edge in edges:

        pg.draw.line(sim_window, (0, 0, 0), actual_points[edge[0]], actual_points[edge[1]], width=2)

    pg.display.update()







