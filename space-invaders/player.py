import pygame
from bullet import Bullet

class Player(pygame.sprite.Sprite):
    def __init__(self, pos, screen_limits, speed):
        super().__init__()
         # load player sprite and convert the surface to the same as the sprite 
         # and improves game performance
        self.image = pygame.image.load("resources/player.png").convert_alpha()
        self.rect = self.image.get_rect(midbottom = pos) 
        self.screen_x_limit = screen_limits
        self.speed = speed
        self.gun_ready = True
        self.gun_time = 0
        self.gun_cooldown = 600
        self.bullets = pygame.sprite.Group()

    def get_player_input(self):
        # left and right movement
        keys = pygame.key.get_pressed()
        if keys[pygame.K_d]:
            self.rect.x += self.speed
        elif keys[pygame.K_a]:
            self.rect.x -= self.speed
        # shooting
        if keys[pygame.K_SPACE] and self.gun_ready:
            self.shoot()
            self.gun_ready = False
            self.gun_time = pygame.time.get_ticks()

    def reload(self):
        if not self.gun_ready:
            current_time = pygame.time.get_ticks()
            if current_time - self.gun_time >= self.gun_cooldown:
                self.gun_ready = True

    def screen_limit(self):
        if self.rect.left <= 0:
            self.rect.left = 0
        if self.rect.right >= self.screen_x_limit:
            self.rect.right = self.screen_x_limit

    def shoot(self):
        self.bullets.add(Bullet(self.rect.center, -8, self.rect.bottom))

    def update(self):
        self.get_player_input()
        self.screen_limit()
        self.reload()
        self.bullets.update()