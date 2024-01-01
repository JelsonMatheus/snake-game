from p5 import *
from collections import deque


class Snake:
    move = Vector(1, 0)

    def __init__(self, cell, score_height):
        x = floor((height - score_height) / cell / 2) * cell
        y = floor(width / cell / 2) * cell
        self.score_height = score_height
        self.position = Vector(x, y)
        self.cell = cell
        self.total = 1
        self.body = deque()
        
    def update(self):
        if self.total != len(self.body):
            self.body.append(self.position)

        # Desloca os elementos do corpo da cobra para a esquerda.
        self.body.rotate(-1)
        if self.total > 0:
            self.body[self.total-1] = self.position
        self.position += self.move * self.cell
    
    def show(self):
        fill(0,255,0)
        for pos in self.body:
            rect(pos.x, pos.y, self.cell, self.cell)
        rect(self.position.x, self.position.y, self.cell, self.cell)

    def key_pressed(self):
        if key == 'UP' and not self.move.y == 1:
            self._dir(0, -1)
        elif key == 'DOWN' and not self.move.y == -1:
            self._dir(0, 1)
        elif key == 'LEFT' and not self.move.x == 1:
            self._dir(-1, 0)
        elif key == 'RIGHT' and not self.move.x == -1:
            self._dir(1, 0)
    
    def eat(self, food:'Food'):
        if food.position.dist(self.position) < 1:
            self.total += 1
            food.set_position()
            return True
        return False
    
    def death(self):
        if self.position.x < 0 or self.position.x >= width:
            return True
        elif self.position.y < (0+self.score_height) or self.position.y >= height:
            return True
        for pos in self.body:
            colision = pos.dist(self.position) < 1
            if colision:
                return True
        return False
    
    def _dir(self, x, y):
        self.move.x = x
        self.move.y = y

class Food:

    def __init__(self, cell, score_height):
        self.score_height = score_height
        self.cell = cell
        self.position = Vector(0, 0)
        self.set_position()
    
    def draw(self):
        fill(255, 0, 0)
        rect(self.position.x, self.position.y, self.cell, self.cell)

    def set_position(self):
        rows = (height - self.score_height) / self.cell
        cols = width / self.cell
        self.position.x = floor(random_uniform(0, cols)) * self.cell
        self.position.y = floor(random_uniform(0, rows)) * self.cell + self.score_height
