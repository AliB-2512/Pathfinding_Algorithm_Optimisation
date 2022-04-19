import math
import pygame
from queue import PriorityQueue
from node import Node

global path_count
path_count = 0
global expanded_count

HEIGHT, WIDTH = 800, 800


def reconstructPath(came_from, current, draw):
    global path_count
    path_count = 0
    while current in came_from:
        path_count = path_count + 1
        current = came_from[current]
        current.makePath()
        draw()


def huresticFunction(intermediate_node, end_node):
    x1, y1 = intermediate_node
    x2, y2 = end_node
    return abs(x1 - x2) + abs(y1 - y2)


def neighbour_calc(startx, starty, endx, endy):
    current_angle = calculate_angle(startx, starty, endx, endy)
    return current_angle


def weighting(start_angle, current_angle, neighbour_row, neighbour_column, grid):
    weightscore = 0
    current_angle

    if neighbour_row >= 47:
        node_ahead = grid[neighbour_row][neighbour_column]
    if neighbour_column >= 47:
        node_ahead = grid[neighbour_row][neighbour_column]
    if neighbour_row <47 and neighbour_column < 47:
        node_ahead = grid[neighbour_row + 2][neighbour_column + 2]

    if start_angle == current_angle:
        weightscore = 10
    elif abs(start_angle - current_angle) >= 5.00:
        weightscore = 1
    elif abs(start_angle - current_angle) >= 2.00:
        weightscore = 4
    elif abs(start_angle - current_angle) <= 1.00:
        weightscore = 8

    if node_ahead.isObstacle():
        weightscore -= 2
    return weightscore


def calculate_angle(startx, starty, endx, endy):
    dx = endx - startx
    dy = endy - starty
    rads = math.atan2(dx, -dy)
    rads %= 2 * math.pi
    degs = math.degrees(rads)
    return degs


def w_aStar(draw, grid, start, end):
    start_angle = calculate_angle(start.row, start.column, end.row, end.column)
    count = 0
    priority_queue = PriorityQueue()
    priority_queue.put((0, count, start))
    came_from = {}
    g_score = {node: math.inf for row in grid for node in row}
    g_score[start] = 0
    f_score = {node: math.inf for row in grid for node in row}
    f_score[start] = huresticFunction(start.getPosition(), end.getPosition())
    open_set = {start}
    while not priority_queue.empty():
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
        current = priority_queue.get()[2]
        open_set.remove(current)
        if current == end:
            reconstructPath(came_from, end, draw)
            return True
        for neighbor in current.neighbors:
            current_angle = neighbour_calc(neighbor.row, neighbor.column, end.row, end.column)
            temp_g_score = g_score[current] + 1
            if temp_g_score < g_score[neighbor]:
                came_from[neighbor] = current
                g_score[neighbor] = temp_g_score
                f_score[neighbor] = temp_g_score + (huresticFunction(
                    neighbor.getPosition(), end.getPosition()
                ) - weighting(start_angle, current_angle, neighbor.row, neighbor.column, grid))
                if neighbor not in open_set:
                    count += 1
                    priority_queue.put((f_score[neighbor], count, neighbor))
                    open_set.add(neighbor)
                    if neighbor != end:
                        neighbor.makeVisiting()
        draw()
        if current != start:
            current.makeVisited()
        global expanded_count
        expanded_count = count
    return False
