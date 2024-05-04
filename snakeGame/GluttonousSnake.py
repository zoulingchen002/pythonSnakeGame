from game import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
import random

SCREEN_WIDTH = 640
SCREEN_HEIGHT = 480

BLOCK_SIZE  = 20

MOVE_DICT = {
    0: ( 1,  0),   # 右
    1: ( 0,  1),   # 下
    2: (-1,  0),   # 左
    3: ( 0, -1)    # 上
}