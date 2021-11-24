import pygame
import random
from pygame import Rect, mixer
pygame.init()

screen_wight = 600
screen_hight = 600

screen = pygame.display.set_mode((screen_wight, screen_hight))
pygame.display.set_caption("Snake")

mixer.music.load('background.wav')
mixer.music.play(-1)

# Collor 
bg = (100,123,150)
body_inner = (50,175,25)
body_outer = (100,100,200)
red = (255,0,0)
foodc = (255,255,255)
blue = (0, 0, 255)
white = (255,255,255)

cell_size= 20
direction = 1
update_snake = 0

# Food 
food =[0,0]
new_food = True
food_place = [0,0]
score = 0 
game_over = False
clicked = False


font = pygame.font.SysFont(None,40)

def draw_screen():
    screen.fill(bg)

def draw_score():
    score_text = "Score : "+str(score)
    score_img = font.render(score_text,True,blue)
    screen.blit(score_img,(5,5))

def check_game_over(game_over):

    # Snakes eat itself 
    head_count =0
    for segment in snake_pos:
        if snake_pos[0] ==segment and head_count>0:
            game_over = True
        head_count +=1
    
    #Chek Touch Boundary
    if snake_pos[0][0]<0 or snake_pos[0][0] > screen_wight or snake_pos[0][1]<0 or snake_pos[0][1] > screen_hight:
        game_over = True
    
    return game_over

# again_reac = Rect(screen_wight//2-80, screen_wight//2+5, 154,40)
again_rect = Rect(screen_wight // 2 - 80, screen_wight // 2, 160, 50)
def draw_game_over():
    ove_text = "Game Over !!!"
    over_img = font.render(ove_text,True,white)
    pygame.draw.rect(screen,blue,(screen_wight//2 -80, screen_hight//2 - 70,194,60),0,10)
    screen.blit(over_img,(screen_wight//2-80,screen_hight//2-50))

    again_txt = "Play Again"
    again_img = font.render(again_txt,True,white)
    pygame.draw.rect(screen, blue, again_rect,0,10)
    screen.blit(again_img, (screen_wight // 2 - 80, screen_hight // 2 + 10))


# Snakes Creat and  Set Positions 
snake_pos = [[int(screen_wight/2),int(screen_hight/2)]]
snake_pos.append([int(screen_wight/2),int(screen_hight/2)+cell_size])
snake_pos.append([int(screen_wight/2),int(screen_hight/2)+cell_size * 2])
snake_pos.append([int(screen_wight/2),int(screen_hight/2)+cell_size * 3 ])




run = True
while run:


    draw_screen()
    draw_score()

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
    # Food 
    if new_food ==True:
        new_food =False
        food[0] = cell_size * random.randint(0,(screen_wight/cell_size)-3)
        food[1] = cell_size * random.randint(0,(screen_hight/cell_size)-3)

    # Draw Food
    pygame.draw.rect(screen,foodc,(food[0],food[1],cell_size,cell_size),0,5)

    if snake_pos[0] == food:
        new_food = True
        new_peice = list(snake_pos[-1])
       
        
        if direction ==1:
            new_peice[1] += cell_size

            explaration_sound = mixer.Sound('laser.wav')
            explaration_sound.play()
        
        if direction ==2:
             new_peice[0] -= cell_size 
             explaration_sound = mixer.Sound('laser.wav')
             explaration_sound.play()

        if direction ==3:
            new_peice[1]-= cell_size
            explaration_sound = mixer.Sound('laser.wav')
            explaration_sound.play()
        if direction ==4:
            new_peice[0]+= cell_size
            explaration_sound = mixer.Sound('laser.wav')
            explaration_sound.play()
        snake_pos.append(new_peice)
        score +=1
        # print(score)



    if game_over == False:
        if update_snake > 80:
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

            game_over= check_game_over(game_over)

    if game_over == True:
            draw_game_over()
            if event.type == pygame.MOUSEBUTTONDOWN and clicked == False:
                clicked = True
            if event.type == pygame.MOUSEBUTTONUP and clicked == True:
                clicked = False
                pos = pygame.mouse.get_pos()
                if again_rect.collidedict(pos):

                #reset variables
                    direction =1
                    update_snake = 0
                    food =[0,0]
                    new_food = True
                    new_piece = [0, 0]
                  
                    score = 0
                    game_over = False

                    # Creat Snake 
                    snake_pos = [[int(screen_wight/2),int(screen_hight/2)]]
                    snake_pos.append([int(screen_wight/2),int(screen_hight/2)+cell_size])
                    snake_pos.append([int(screen_wight/2),int(screen_hight/2)+cell_size * 2])
                    snake_pos.append([int(screen_wight/2),int(screen_hight/2)+cell_size * 3 ])


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

