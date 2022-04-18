import math
import pygame
from queue import PriorityQueue
from node import Node

global path_count
path_count = 0
global expanded_count

HEIGHT, WIDTH = 900, 900


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
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
        current = priority_queue.get()[1]

        if visited[current]:
            continue
        visited[current] = True
        if current == end:
            reconstructPath(came_from, end, draw)
            return True
        if current != start:
            current.makeVisited()
        for neighbor in current.neighbors:
            weight = 1
            if distance[current] + weight < distance[neighbor]:
                came_from[neighbor] = current
                distance[neighbor] = distance[current] + weight
                priority_queue.put((distance[neighbor], neighbor))
            if neighbor != end and neighbor != start and not visited[neighbor]:
                count += 1
                neighbor.makeVisiting()
        draw()
        global expanded_count
        expanded_count = count
    return False
