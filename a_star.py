import math
import pygame
from queue import PriorityQueue
from node import Node

global path_count
path_count = 0
global searched_count


HEIGHT, WIDTH = 800, 800


def reconstructPath(came_from, current, draw):
    global path_count
    path_count = 0
    while current in came_from:
        path_count = path_count + 1
        current = came_from[current]
        current.makePath()
        draw()


def heuristicFunction(intermediate_node, end_node):
    x1, y1 = intermediate_node
    x2, y2 = end_node
    return abs(x1 - x2) + abs(y1 - y2)


def aStar(draw, grid, start, end):
    count = 0
    priority_queue = PriorityQueue()
    priority_queue.put((0, count, start))
    came_from = {}
    g_score = {node: math.inf for row in grid for node in row}
    g_score[start] = 0
    f_score = {node: math.inf for row in grid for node in row}
    f_score[start] = heuristicFunction(start.getPosition(), end.getPosition())
    open_set = {start}
    while not priority_queue.empty():

        current = priority_queue.get()[2]
        open_set.remove(current)
        if current == end:
            reconstructPath(came_from, end, draw)
            return True
        for neighbour in current.neighbours:
            temp_g_score = g_score[current] + 1
            if temp_g_score < g_score[neighbour]:
                came_from[neighbour] = current
                g_score[neighbour] = temp_g_score
                f_score[neighbour] = temp_g_score + heuristicFunction(
                    neighbour.getPosition(), end.getPosition()
                )
                if neighbour not in open_set:
                    count += 1
                    priority_queue.put((f_score[neighbour], count, neighbour))
                    open_set.add(neighbour)
                    if neighbour != end:
                        neighbour.makeVisiting()
        draw()
        if current != start:
            current.makeVisited()
        global searched_count
        searched_count = count
    return False
