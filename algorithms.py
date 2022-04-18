from random import randint

import pygame
from node import Node
from a_star import aStar
from dijkstra import dijkstra

pygame.init()

HEIGHT, WIDTH = 900, 900
window = pygame.display.set_mode((HEIGHT, WIDTH))
pygame.display.set_caption("Pathfinding visualizer")

GREY = (128, 128, 128)


def generate_num(x, y):
    return randint(x, y)


def algorithm(draw, grid, start, end, algorithm_type):
    if algorithm_type == 1:
        aStar(draw, grid, start, end)
    elif algorithm_type == 2:
        dijkstra(draw, grid, start, end)


def buildGrid(row, width):
    grid = []
    node_width = width // row
    for i in range(row):
        grid.append([])
        for j in range(row):
            grid[i].append(Node(i, j, node_width, row))
    return grid


def drawGridLines(window, rows, width):
    gap = width // rows
    for i in range(rows):
        pygame.draw.line(window, GREY, (0, i * gap), (width, i * gap))
        pygame.draw.line(window, GREY, (i * gap, 0), (i * gap, width))


def draw(window, grid, rows, width):
    for row in grid:
        for node in row:
            node.draw(window)
    drawGridLines(window, rows, width)
    pygame.display.update()


def getClickedPosition(position, rows, width):
    gap = width // rows
    x, y = position
    row, column = x // gap, y // gap
    return row, column


def main(window, WIDTH, density, algorithm_type):
    rows = 50
    grid = buildGrid(rows, WIDTH)

    start, end = None, None

    for x in range(0, density):
        row_pos = generate_num(0, rows - 1)
        col_pos = generate_num(0, rows - 1)
        node = grid[row_pos][col_pos]
        if not start and node != end:
            start = node
            start.makeStartNode()

        elif not end and node != start:
            end = node
            end.makeEndNode()

        elif node != end and node != start:
            node.makeObstacle()

    for row in grid:
        for node in row:
            node.updateNeighbors(grid)

    algorithm(lambda: draw(window, grid, rows, WIDTH), grid, start, end, algorithm_type)
    grid = buildGrid(rows, WIDTH)
