from PyQt5.QtGui import *

class Snake:
    def __init__(self, x, y, direction):
        self.x = x
        self.y = y
        self.direction = direction
        self.body = [(x, y)]