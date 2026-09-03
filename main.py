import pygame, sys, random
from game import Game
from spaceship import Spaceship
from obstacle import Obstacle
from laser import Laser
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

SHOOT_LASER = pygame.USEREVENT
pygame.time.set_timer(SHOOT_LASER, 300)

MYSTERYSHIP = pygame.USEREVENT + 1
pygame.time.set_timer(MYSTERYSHIP, random.randint(12000, 24000)) 
 
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        
        if event.type == SHOOT_LASER:
            game.alien_shoot_laser()
        if event.type == MYSTERYSHIP:
            game.create_mystery_ship()
            pygame.time.set_timer(MYSTERYSHIP, random.randint(12000, 24000))  
 
    # updating spaceship
        game.update() # game update
        game.spaceship_group.update()
        spaceship_group.update()
        game.move_aliens()
        game.alien_lasers_group.update()
        game.mysteryship_group.update()
        game.check_for_collision()
 
    # Drawing
    screen.fill(GREY)
    game.spaceship_group.draw(screen)
    game.spaceship_group.sprite.lasers.draw(screen)
    for obstacle in game.obstacles:
        obstacle.block_group.draw(screen)
    game.alien_group.draw(screen)
    game.alien_lasers_group.draw(screen)
    game.mysteryship_group.draw(screen)
    pygame.display.update()
    clock.tick(60)
 
 
