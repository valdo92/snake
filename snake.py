
import random
import sys
import pygame
import numpy as np


pygame.init()
screen = pygame.display.set_mode([1200, 600])
clock = pygame.time.Clock()
screen.fill([0,0,0])

 ### damier ###
x=np.arange(0,60)  
y=np.arange(0,30)
for k in x:
    for i in y:
        if (i+k)%2==0: # trouver la relation entre (x,y) et la couleur de la case
            width = 20     
            height = 20
            rect = [20*k,20*i, width, height]
            red = 255
            green = 255
            blue = 255
            color = [red, green, blue]
            pygame.draw.rect(screen, color, rect)

a,b=(60,200)
c,d=(40,200)
e,f=(20,200)

for x,y in [(a-40,b),(a-20,b),(a,b)]:
    width = 20
    height = 20
         
    rect = [x,y, width, height]
    red = 0
    green = 0
    blue = 255
    color = [red, green, blue]
    pygame.draw.rect(screen, color, rect)

fruit_x=np.random.randint(0,59)*20
fruit_y=np.random.randint(0,29)*20
snake=[[e,f],[c,d],[a,b]]
    

def draw_blanc(x,y):
    width = 20
    height = 20
    rect = [x,y, width, height]
    red = 255
    green = 255
    blue = 255
    color = [red, green, blue]
    pygame.draw.rect(screen, color, rect)
    pygame.display.update()

def draw_blue(x,y):
    width = 20
    height = 20
    rect = [x,y, width, height]
    red = 0
    green = 0
    blue = 255
    color = [red, green, blue]
    pygame.draw.rect(screen, color, rect)
    pygame.display.update()

def draw_noir(x,y): 
    width = 20
    height = 20
    rect = [x,y, width, height]
    red = 0
    green = 0
    blue = 0
    color = [red, green, blue]
    pygame.draw.rect(screen, color, rect)
    pygame.display.update()

direction=[1,0]

def move(direction):
    if ((snake[0][0]+snake[0][1])/20)%2==0:
        draw_blanc(snake[0][0],snake[0][1])
    else : 
        draw_noir(snake[0][0],snake[0][1])
    for i in range (len(snake)-1):
        snake[i][0]=snake[i+1][0]
        snake[i][1]=snake[i+1][1]

    snake[len(snake)-1][0]+=direction[0]*20
    snake[len(snake)-1][1]+=direction[1]*20

    draw_blue(snake[len(snake)-1][0],snake[len(snake)-1][1])


def draw_rouge(x,y):
    width = 20
    height = 20
    rect = [x,y, width, height]
    red = 255
    green = 0
    blue = 0
    color = [red, green, blue]
    pygame.draw.rect(screen, color, rect)
    pygame.display.update()

draw_rouge(fruit_x,fruit_y)

while True:
    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:

                #if a,b==e,f:
                    #loose je reviens sur moi même
                direction=[0,-1]
                
                pygame.display.update()
                print('↑')



            elif event.key == pygame.K_DOWN:
                direction = [0,1]
                

            elif event.key == pygame.K_RIGHT :
                direction = [1,0]
                
                pygame.display.update()
                print('→')

            elif event.key == pygame.K_LEFT:
                direction = [-1,0]
                
                pygame.display.update()
                print('←')
 
 
    move(direction)
    if snake[len(snake)-1][0]==fruit_x and snake[len(snake)-1][1]==fruit_y:
    
        fruit_x=np.random.randint(0,59)*20
        fruit_y=np.random.randint(0,29)*20
        draw_rouge(fruit_x,fruit_y)
        a=snake[0][0]-direction[0]*20
        b=snake[0][1]-direction[1]*20
        snake = [[a,b]]+snake

    elif snake[len(snake)-1][0]>1200 or snake[len(snake)-1][0]<0 or snake[len(snake)-1][1]>600 or snake[len(snake)-1][1]<0 :
        pygame.quit()
        sys.exit()

    for j in range (len(snake)-1):
        if snake[j][0]==snake[len(snake)-1][0] and snake[j][1]==snake[len(snake)-1][1]:
            pygame.quit()
            sys.exit()

    pygame.display.update()
    clock.tick(6)


