import pygame, sys
from player import Player

WIDTH = 800
HEIGHT = 600

class Game:
    def __init__(self):
        player_sprite = Player((WIDTH / 2, HEIGHT - 10), WIDTH, 5)
        self.player = pygame.sprite.GroupSingle(player_sprite)

    def run(self):
        self.player.sprite.bullets.draw(screen)
        self.player.draw(screen)
        self.player.update()

# Init screen and start gameloop
if __name__ == '__main__':
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    clock = pygame.time.Clock()
    game = Game()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        screen.fill((0,0,0)) # black background
        game.run()
        pygame.display.flip() 
        clock.tick(75) #60hz screen