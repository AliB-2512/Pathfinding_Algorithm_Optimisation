import pygame

HEIGHT, WIDTH = 800, 800

RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
PURPLE = (128, 0, 128)
ORANGE = (255, 165, 0)
GREY = (128, 128, 128)
CYAN = (0, 255, 255)


class Node:
    def __init__(self, row, column, width, total_rows):
        self.row = row
        self.column = column
        self.x = row * width
        self.y = column * width
        self.colour = WHITE
        self.width = width
        self.neighbours = []
        self.total_rows = total_rows

    def getPosition(self):
        return self.row, self.column

    def isCLosed(self):
        return self.colour == RED

    def isVisiting(self):
        return self.colour == GREEN

    def isObstacle(self):
        return self.colour == BLACK

    def isStartNode(self):
        return self.colour == ORANGE

    def isEndNode(self):
        return self.colour == CYAN

    def isPath(self):
        return self.colour == PURPLE

    def resetNode(self):
        self.colour = WHITE

    def makeStartNode(self):
        self.colour = ORANGE

    def makeEndNode(self):
        self.colour = CYAN

    def makeVisited(self):
        self.colour = RED

    def makeVisiting(self):
        self.colour = GREEN

    def makeObstacle(self):
        self.colour = BLACK

    def makePath(self):
        self.colour = PURPLE

    def draw(self, window):
        pygame.draw.rect(window, self.colour, (self.x, self.y, self.width, self.width))

    def updateNeighbours(self, grid):
        self.neighbours = []
        if (
                self.row < self.total_rows - 1
                and not grid[self.row + 1][self.column].isObstacle()
        ):
            self.neighbours.append(grid[self.row + 1][self.column])
        if self.row > 0 and not grid[self.row - 1][self.column].isObstacle():
            self.neighbours.append(grid[self.row - 1][self.column])
        if (
                self.column < self.total_rows - 1
                and not grid[self.row][self.column + 1].isObstacle()
        ):
            self.neighbours.append(grid[self.row][self.column + 1])
        if self.column > 0 and not grid[self.row][self.column - 1].isObstacle():
            self.neighbours.append(grid[self.row][self.column - 1])

    def __lt__(self, other):
        return False
