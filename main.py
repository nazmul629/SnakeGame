import pygame
pygame.init()

screen_wight = 600
screen_hight = 600

screen = pygame.display.set_mode((screen_wight, screen_hight))
pygame.display.set_caption("Snake")

# Collor 
bg = (100,123,150)
body_inner = (50,175,25)
body_outer = (100,100,200)
red = (255,0,0)

def draw_screen():
    screen.fill(bg)

cell_size= 20
direction = 1
update_snake = 0




snake_pos = [[int(screen_wight/2),int(screen_hight/2)]]
snake_pos.append([int(screen_wight/2),int(screen_hight/2)+cell_size])
snake_pos.append([int(screen_wight/2),int(screen_hight/2)+cell_size * 2])
snake_pos.append([int(screen_wight/2),int(screen_hight/2)+cell_size * 3 ])

run = True
while run:

    draw_screen()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

        elif event.type ==pygame.KEYDOWN:
            if event.key == pygame.K_UP and direction != 3:
                direction = 1
            if  event.key == pygame.K_DOWN and direction != 1:
                direction = 3
            if event.key == pygame.K_RIGHT and direction != 4:
                direction = 2
            if  event.key == pygame.K_LEFT and direction != 2:
                direction = 4

    if update_snake > 99:
        update_snake = 0
        snake_pos = snake_pos[-1:] + snake_pos[:-1]
        if direction == 1:
            snake_pos[0][0] = snake_pos[1][0]
            snake_pos[0][1] = snake_pos[1][1] - cell_size
			#heading down
        if direction == 3:
            snake_pos[0][0] = snake_pos[1][0]
            snake_pos[0][1] = snake_pos[1][1] + cell_size
			#heading right
        if direction == 2:
            snake_pos[0][1] = snake_pos[1][1]
            snake_pos[0][0] = snake_pos[1][0] + cell_size
			#heading left
        if direction == 4:
            snake_pos[0][1] = snake_pos[1][1]
            snake_pos[0][0] = snake_pos[1][0] - cell_size

            


   

    head = 1
    for x in snake_pos:
        if head ==0:
            pygame.draw.rect(screen,body_outer,(x[0],x[1],cell_size,cell_size))
            pygame.draw.rect(screen,body_inner,(x[0]+1,x[1]+1,cell_size-2,cell_size-2)) 

        if head ==1:
            pygame.draw.rect(screen,body_outer,(x[0],x[1],cell_size,cell_size))
            pygame.draw.rect(screen,red,(x[0]+1,x[1]+1,cell_size-2,cell_size-2))
            head =0

    pygame.display.update()
    update_snake += 1
pygame.quit()

