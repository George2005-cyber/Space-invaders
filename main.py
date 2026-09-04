import pygame, sys, random
from game import Game
pygame.init()

SCREEN_WIDTH = 730 # screen size
SCREEN_HEIGHT = 715
OFFSET = 60


GREY = (29, 29, 27)
YELLOW = (243, 216, 63)

font = pygame.font.Font("font/monogram.ttf", 40)
level_surface = font.render("LEVEL 01", False, YELLOW)
game_over_surface = font.render("GAME OVER", False, YELLOW)
score_text_surface = font.render("SCORE", False, YELLOW)
highscore_text_surface = font.render("HIGH-SCORE", False, YELLOW)

screen = pygame.display.set_mode((SCREEN_WIDTH + OFFSET, SCREEN_HEIGHT + 2*OFFSET))
background = pygame.image.load("images/background 2.jpg").convert()
backgroung =  pygame.transform.scale(background, (SCREEN_WIDTH + OFFSET, SCREEN_HEIGHT + 2*OFFSET))
pygame.display.set_caption("Python Space Invaders")

clock = pygame.time.Clock()

game = Game(SCREEN_WIDTH, SCREEN_HEIGHT, OFFSET)


SHOOT_LASER = pygame.USEREVENT
pygame.time.set_timer(SHOOT_LASER, 300)  # Trigger every 1 second

MYSTERYSHIP = pygame.USEREVENT + 1
pygame.time.set_timer(MYSTERYSHIP, random.randint(4000, 8000))  # Trigger every 4-8 seconds

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if event.type == SHOOT_LASER and game.run:
            game.alien_shoot_laser()

        if event.type == MYSTERYSHIP and game.run:
            game.create_mysteryship()
            pygame.time.set_timer(MYSTERYSHIP, random.randint(4000, 8000))  # Reset timer for next mystery ship

        keys = pygame.key.get_pressed()
        if keys[pygame.K_SPACE] and game.run == False:
            game.reset()

    # updating spaceship
    if game.run:
        game.spaceship_group.update()
        game.move_aliens()
        game.alien_lasers_group.update()
        game.mysteryship_group.update()
        game.check_for_collisions()

    # Drawing
    screen.blit(background, (0, 0))
    #screen.fill(GREY)
    pygame.draw.rect(screen, YELLOW, (10, 10, 780, 780), 2, 0, 60, 60, 60, 60)
    pygame.draw.line(screen, YELLOW, (25, 730), (775, 730), 3)

    if game.run:
        screen.blit(level_surface, (570, 740, 50, 50))
    else:
        screen.blit(game_over_surface, (570, 740, 50, 50))

    x = 50
    for life in range(game.lives):
        screen.blit(game.spaceship_group.sprite.image, (x, 745 ))   
        x += 50

    screen.blit(score_text_surface, (50, 15, 50, 50))
    formatted_score = str(game.score).zfill(5)
    score_surface = font.render(formatted_score, False, YELLOW)
    screen.blit(score_surface, (50, 40, 50, 50))
    screen.blit(highscore_text_surface, (550, 15, 50, 50))
    formatted_highscore = str(game.highscore).zfill(5)
    highscore_surface = font.render(formatted_highscore, False, YELLOW)
    screen.blit(highscore_surface, (625, 40, 50, 50))


    game.spaceship_group.draw(screen)
    game.spaceship_group.sprite.lasers.draw(screen)
    for obstacle in game.obstacles:
        obstacle.block_group.draw(screen)
    game.aliens_group.draw(screen)
    game.alien_lasers_group.draw(screen)
    game.mysteryship_group.draw(screen)
    
    pygame.display.update()
    clock.tick(60)

