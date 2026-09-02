import pygame 
from spaceship import Spaceship
from obstacle import obstacle
from obstacle import grid

SCREEN_WIDTH = 500
SCREEN_HEIGHT = 500

class game:
    def __init__(self):
        self.screen_width = SCREEN_WIDTH
        self.screen_height = SCREEN_HEIGHT
        self.spaceship_group = pygame.sprite.GroupSingle()
        self.spaceship_group.add(Spaceship(self.screen_width, self.screen_height))
        self.obstacles = self.create_obstacle()
        def create_obstacle(self, x, y):
            obstacle_width = len(grid[0]) * 3
            gap = (self.screen_width - (4 * obstacle_width)) / 5
            obstacle = [ ]
            for i in range(4):
                offset_x =(i + 1) * gap + i * obstacle_width
                obstacle.Obstacle(offset_x, self.screen_height - 100)
                obstacle.append(obstacle)
                return obstacle
