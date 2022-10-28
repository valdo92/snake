
import random
import sys
import pygame
import numpy as np


pygame.init()
screen = pygame.display.set_mode([600, 600])
clock = pygame.time.Clock()
screen.fill([250,250,250])
def serpent(a,b):
        for x,y in [(a-30,b),(a-15,b),(a,b)]:
            width = 30
            height = 30
            rect = [x,y, width, height]
            red = 0
            green = 255
            blue = 0
            color = [red, green, blue]
            pygame.draw.rect(screen, color, rect)
a,b=(70,400)
c,d=(40,400)
e,f=(10,400)
serpent(a,b)    


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                x,y=e,f
                width = 30
                height = 30
                rect = [x,y, width, height]
                red = 255
                green = 255
                blue = 255
                color = [red, green, blue]
                pygame.draw.rect(screen, color, rect)
                e,f=c,d
                c,d=a,b
                b+=-30

                #if a,b==e,f:
                    #loose je reviens sur moi même

                width = 30
                height = 30
                rect = [a,b, width, height]
                red = 0
                green = 255
                blue = 0
                color = [red, green, blue]
                pygame.draw.rect(screen, color, rect)
                

                print('↑')
            elif event.key == pygame.K_DOWN:
                x,y=e,f
                width = 30
                height = 30
                rect = [x,y, width, height]
                red = 255
                green = 255
                blue = 255
                color = [red, green, blue]
                pygame.draw.rect(screen, color, rect)
                e,f=c,d
                c,d=a,b
                b+=30

                #if a,b==e,f:
                    #loose je reviens sur moi même

                width = 30
                height = 30
                rect = [a,b, width, height]
                red = 0
                green = 255
                blue = 0
                color = [red, green, blue]
                pygame.draw.rect(screen, color, rect)
                
            elif event.key == pygame.K_RIGHT :
                x,y=e,f
                width = 30
                height = 30
                rect = [x,y, width, height]
                red = 255
                green = 255
                blue = 255
                color = [red, green, blue]
                pygame.draw.rect(screen, color, rect)
                e,f=c,d
                c,d=a,b
                a+=30

                #if a,b==e,f:
                    #loose je reviens sur moi même

                width = 30
                height = 30
                rect = [a,b, width, height]
                red = 0
                green = 255
                blue = 0
                color = [red, green, blue]
                pygame.draw.rect(screen, color, rect)
                
                
                print('→')
            elif event.key == pygame.K_LEFT:
                x,y=e,f
                width = 30
                height = 30
                rect = [x,y, width, height]
                red = 255
                green = 255
                blue = 255
                color = [red, green, blue]
                pygame.draw.rect(screen, color, rect)
                e,f=c,d
                c,d=a,b
                a+=-30

                #if a,b==e,f:
                    #loose je reviens sur moi même

                width = 30
                height = 30
                rect = [a,b, width, height]
                red = 0
                green = 255
                blue = 0
                color = [red, green, blue]
                pygame.draw.rect(screen, color, rect)
                
                
                print('←')
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
     

    pygame.display.update()
    clock.tick(1)


