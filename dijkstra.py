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


def dijkstra(draw, grid, start, end):
    count = 0
    visited = {node: False for row in grid for node in row}
    distance = {node: math.inf for row in grid for node in row}
    distance[start] = 0
    came_from = {}
    priority_queue = PriorityQueue()
    priority_queue.put((0, start))
    while not priority_queue.empty():
        current = priority_queue.get()[1]

        if visited[current]:
            continue
        visited[current] = True
        if current == end:
            reconstructPath(came_from, end, draw)
            return True
        if current != start:
            current.makeVisited()
        for neighbour in current.neighbours:
            weight = 1
            if distance[current] + weight < distance[neighbour]:
                came_from[neighbour] = current
                distance[neighbour] = distance[current] + weight
                priority_queue.put((distance[neighbour], neighbour))
            if neighbour != end and neighbour != start and not visited[neighbour]:
                count += 1
                neighbour.makeVisiting()
        draw()
        global searched_count
        searched_count = count
    return False
