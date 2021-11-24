import pygame
pygame.init()

screen_wight = 600
screen_hight = 600

screen = pygame.display.set_mode((screen_wight, screen_hight))
pygame.display.set_caption("Snake")


run = True
while run:


    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

            
    pygame.display.update()
pygame.quit()

