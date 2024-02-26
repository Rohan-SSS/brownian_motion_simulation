import numpy as np
# Models
class Robot:
    def __init__(self, x, y, direction, speed):
        self.x = x
        self.y = y
        self.direction = direction
        self.speed = speed

    # collision rotation
    def update_position(self, time_step):
        dx = np.cos(self.direction) * self.speed * time_step
        dy = np.sin(self.direction) * self.speed * time_step
        self.x += dx
        self.y += dy

class Arena:
    def __init__(self, width, height):
        self.width = width + 2
        self.height = height + 2

    def contains(self, robot):
        return 0 <= robot.x < self.width and 0 <= robot.y < self.height
