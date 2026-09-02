import pygame, sys
from game import Game
from spaceship import Spaceship
from obstacle import Obstacle
pygame.init()
 
SCREEN_WIDTH = 500 # screen size
SCREEN_HEIGHT = 500
 
 
GREY = (29, 29, 27)
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Python Space Invaders")
 
clock = pygame.time.Clock()
game = Game(SCREEN_WIDTH, SCREEN_HEIGHT)
 
spaceship = Spaceship(SCREEN_WIDTH, SCREEN_HEIGHT)
spaceship_group = pygame.sprite.GroupSingle()
spaceship_group.add(spaceship)
 
obstacle = Obstacle(x=100, y=SCREEN_HEIGHT - 100) 
 
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
 
    # updating spaceship
    game.spaceship_group.update()
    spaceship_group.update()
   
 
    # Drawing
    screen.fill(GREY)
    game.spaceship_group.draw(screen)
    game.spaceship_group.sprite.lasers.draw(screen)
    
    for obstacle in game.obstacles:
        obstacle.block_group.draw(screen)
    pygame.display.update()
    clock.tick(60)
 
 
