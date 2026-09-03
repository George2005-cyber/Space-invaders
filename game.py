import pygame, random 
from spaceship import Spaceship
from obstacle import Obstacle
from obstacle import grid
from aliens import Alien
from laser import Laser
from aliens import Mysteryship

SCREEN_WIDTH = 500
SCREEN_HEIGHT = 500

class Game:
    def __init__(self, screen_width, screen_height):
        self.screen_width = screen_width
        self.screen_height = screen_height
        self.spaceship_group = pygame.sprite.GroupSingle()
        self.spaceship_lasers_group = pygame.sprite.Group()
        self.spaceship_group.add(Spaceship(self.screen_width, self.screen_height))
        self.obstacles = self.create_obstacle()
        self.alien_group = pygame.sprite.Group()
        self.create_aliens()
        self.alien_direction = 1
        self.alien_lasers_group = pygame.sprite.Group()
        self.mysteryship_group = pygame.sprite.Group()
        self.lives = 3
        

    def create_obstacle(self):
        obstacle_width = len(grid[0]) * 3
        gap = (self.screen_width - (4 * obstacle_width)) / 5
        obstacles = []
        for i in range(4):
            offset_x = (i + 1) * gap + i * obstacle_width
            obstacle = Obstacle(offset_x, self.screen_height - 100)
            obstacles.append(obstacle)
        return obstacles

    def create_aliens(self):
        for row in range(5):
            for column in range(11):
                x = 10 + column * 40
                y = 20 + row * 40

                if row == 0:
                     alien_type = 3
                elif row in (1, 2):

                   alien_type = 2
                else:
                    alien_type = 1

                alien = Alien(alien_type, x, y)
                self.alien_group.add(alien)
    def move_aliens(self):  
        self.alien_group.update(self.alien_direction)       

        alien_sprites = self.alien_group.sprites()
        edge_hit = False
        for alien in alien_sprites:
            if alien.rect.right >= self.screen_width or alien.rect.left <= 0:
                edge_hit = True
            if edge_hit:
                self.alien_direction *= -1
                self.alien_shoot_down(2)
                break
    def alien_shoot_down(self, distance):
        for alien in self.alien_group.sprites():
            alien.rect.y += distance
    def alien_shoot_laser(self):
        if self.alien_group.sprites():
            random_alien = random.choice(self.alien_group.sprites())
            laser_sprite = Laser(random_alien.rect.center, -6, self.screen_height)
            self.alien_lasers_group.add(laser_sprite)

    def create_mystery_ship(self):
             self.mysteryship_group.add(Mysteryship(self.screen_width))

    def check_for_collision(self):
         #spaceship
         if self.spaceship_group.sprite.lasers:
             for laser_sprite in self.spaceship_group.sprite.lasers:
              if pygame.sprite.spritecollide(laser_sprite, self.alien_group, True):
                    laser_sprite.kill()
              if pygame.sprite.spritecollide(laser_sprite, self.mysteryship_group, True):
                    laser_sprite.kill()
              for obstacle in self.obstacles:
                    if pygame.sprite.spritecollide(laser_sprite, obstacle.block_group, True):
                        laser_sprite.kill()
             #Alien lasers
         if self.alien_group:
                for alien_laser in self.alien_lasers_group:
                    if pygame.sprite.spritecollide(alien_laser,self.spaceship_group, False):
                        alien_laser.kill()
                        self.lives -= 1
                        print(f"Hit! Lives remaining: {self.lives}")
                        if self.lives <= 0:
                            print("Game Over!")
                            pygame.quit()
                            exit()
                    for obstacle in self.obstacles:
                        if pygame.sprite.spritecollide(alien_laser, obstacle.block_group, True):
                            alien_laser.kill()    
               #Aliens hitting barries
         if self.alien_group:
                for alien in self.alien_group:
                    for obstacle in self.obstacles:
                        pygame.sprite.spritecollide(alien, obstacle.block_group, True)
                    if pygame.sprite.spritecollide(alien, self.spaceship_group, False):
                        print("Game Over! Aliens reached the spaceship.")
                        pygame.quit()
                        exit()
         