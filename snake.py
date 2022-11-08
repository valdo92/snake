
import random
import sys
import pygame
import numpy as np


pygame.init()
screen = pygame.display.set_mode([600, 600])
clock = pygame.time.Clock()
screen.fill([250,250,250])

a,b=(70,400)
c,d=(40,400)
e,f=(10,400)

for x,y in [(a-60,b),(a-30,b),(a,b)]:
    width = 30
    height = 30
         
    rect = [x,y, width, height]
    red = 0
    green = 0
    blue = 0
    color = [red, green, blue]
    pygame.draw.rect(screen, color, rect)


snake=[[e,f],[c,d],[a,b]]
    

def draw_blanc(x,y):
    width = 30
    height = 30
    rect = [x,y, width, height]
    red = 255
    green = 255
    blue = 255
    color = [red, green, blue]
    pygame.draw.rect(screen, color, rect)
    pygame.display.update()

def draw_noir(x,y): 
    width = 30
    height = 30
    rect = [x,y, width, height]
    red = 0
    green = 0
    blue = 0
    color = [red, green, blue]
    pygame.draw.rect(screen, color, rect)
    pygame.display.update()

direction=[1,0]

def move(direction):
    draw_blanc(snake[0][0],snake[0][1])
    for i in range (len(snake)-1):
        snake[i][0]=snake[i+1][0]
        snake[i][1]=snake[i+1][1]

    snake[len(snake)-1][0]+=direction[0]*30
    snake[len(snake)-1][1]+=direction[1]*30

    draw_noir(snake[len(snake)-1][0],snake[len(snake)-1][1])



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
 
 ### damier ###
 #   x=np.arange(0,20)  
 #  y=np.arange(0,20)
 #   for k in x:
  #      for i in y:
  #          if (i+k)%2==0: # trouver la relation entre (x,y) et la couleur de la case
#
 #               width = 30
  #              height = 30
   #             rect = [30*i,30*k, width, height]
     #           red = 255
    #            green = 255
   #             blue = 255
 # #              color = [red, green, blue]
 #               pygame.draw.rect(screen, color, rect)

### créer le serpent 
    move(direction)
    pygame.display.update()
    clock.tick(1)


