"""
Player class.
"""
from time import time

class Player:
    def __init__(self, x: int, y: int, direction: str = "right"):
        self.x = x
        self.y = y
        self.direction = direction
        self.alive = True
        self.saved = False
        self.falling = False
        self.umbrella = False
        self.stairs_r = False
        self.stairs_l = False
        self.blocker = False
        self.blocker_idx = None
        self.speed = 1  # Default speed (1px)

        self.img = (0, 32, 16, 16, 16, 0)
        # self.img2 = (0, 16, 56, 16, 16, 0)
