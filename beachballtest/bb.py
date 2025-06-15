import pygame, sys

pygame.init()

screen_size = WIDTH, HEIGTH = 1024, 768
speed = [1, 1]
black = 0, 0, 0

screen = pygame.display.set_mode([WIDTH, HEIGTH])
ball = pygame.image.load("ball.gif")
ballrect = ball.get_rect()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()
    
    ballrect = ballrect.move(speed)
    if ballrect.left < 0 or ballrect.right > WIDTH:
        speed[0] = -speed[0]
    if ballrect.top < 0 or ballrect.bottom > HEIGTH:
        speed[1] = -speed[1]

    screen.fill(black)
    screen.blit(ball, ballrect)
    pygame.display.flip()



