import random
import sys
import pygame
import numpy as np


### Constante ###

width = 20  # largeur
height = 20

FPS = 6  # frames per seconde

black = [0, 0, 0]
white = [255, 255, 255]
red = [255, 0, 0]
blue = [0, 0, 255]
COLORS = {"background": white, "snake": blue, "fruit": red}


UP = [0, -1]
DOWN = [0, 1]
LEFT = [-1, 0]
RIGHT = [1, 0]

SCORE = 0


### Game State ###

snake = [[20, 200], [40, 200], [60, 200]]  # position serpent initiale

direction = [0, 1]  # direction initiale

fruit_x = np.random.randint(0, 59) * 20  # position fruit initale
fruit_y = np.random.randint(0, 29) * 20


### Helper Fonction ###


def draw_blanc(x, y):
    rect = [x, y, width, height]
    pygame.draw.rect(screen, white, rect)
    pygame.display.update()


def draw_blue(x, y):
    rect = [x, y, width, height]
    pygame.draw.rect(screen, blue, rect)
    pygame.display.update()


def draw_noir(x, y):
    rect = [x, y, width, height]
    pygame.draw.rect(screen, black, rect)
    pygame.display.update()


def draw_rouge(x, y):
    rect = [x, y, width, height]
    pygame.draw.rect(screen, red, rect)
    pygame.display.update()


def move(direction):
    if ((snake[0][0] + snake[0][1]) / 20) % 2 == 0:
        draw_blanc(snake[0][0], snake[0][1])
    else:
        draw_noir(snake[0][0], snake[0][1])
    for i in range(len(snake) - 1):
        snake[i][0] = snake[i + 1][0]
        snake[i][1] = snake[i + 1][1]

    snake[len(snake) - 1][0] += direction[0] * 20
    snake[len(snake) - 1][1] += direction[1] * 20

    draw_blue(snake[len(snake) - 1][0], snake[len(snake) - 1][1])


def damier():
    screen.fill([0, 0, 0])  # configuration de l'arrière plan en damier
    x = np.arange(0, 60)
    y = np.arange(0, 30)
    for k in x:
        for i in y:
            if (
                i + k
            ) % 2 == 0:  # trouver la relation entre (x,y) et la couleur de la case
                rect = [20 * k, 20 * i, width, height]
                pygame.draw.rect(screen, white, rect)


def save_state():
    state = {
        "snake": snake,
        "direction": direction,
        "fruit": [fruit_x, fruit_y],
        "score": SCORE,
    }
    with open("SNAPSHOT", mode="w", encoding="utf-8") as file:
        file.write(repr(state))


def load_state():
    global snake, direction, fruit_x, fruit_y, SCORE

    with open("SNAPSHOT", mode="r", encoding="utf-8") as file:
        data = file.read()

    state = eval(data)
    snake = state["snake"]
    direction = state["direction"]
    fruit_x = state["fruit"][0]
    fruit_y = state["fruit"][1]
    SCORE = state["score"]


def handle_event():
    for event in pygame.event.get():
        global direction, FPS

        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        elif event.type == pygame.KEYDOWN:

            if event.key == pygame.K_UP:

                direction = UP
                pygame.display.update()
                print("↑")

            elif event.key == pygame.K_DOWN:

                direction = DOWN

            elif event.key == pygame.K_RIGHT:

                direction = RIGHT
                pygame.display.update()
                print("→")

            elif event.key == pygame.K_LEFT:

                direction = LEFT
                pygame.display.update()
                print("←")

            elif event.key == pygame.K_s:
                save_state()

            elif event.key == pygame.K_l:
                load_state()

            elif event.key == pygame.K_v:
                FPS += 1

            elif event.key == pygame.K_r:
                FPS -= 1


def eat_fruit():
    global fruit_x, fruit_y, snake, SCORE

    if snake[len(snake) - 1][0] == fruit_x and snake[len(snake) - 1][1] == fruit_y:

        fruit_x = np.random.randint(0, 59) * 20
        fruit_y = np.random.randint(0, 29) * 20

        draw_rouge(fruit_x, fruit_y)

        a = snake[0][0] - direction[0] * 20
        b = snake[0][1] - direction[1] * 20
        snake = [[a, b]] + snake

        SCORE += 1


def wait_for_next_time(FPS):
    clock.tick(FPS)


def exit():
    pygame.quit()
    sys.exit()


def snake_die():
    global snake

    if (
        snake[len(snake) - 1][0] > 1199
        or snake[len(snake) - 1][0] < 0
        or snake[len(snake) - 1][1] > 599
        or snake[len(snake) - 1][1] < 0
    ):
        exit()

    for j in range(len(snake) - 1):
        if (
            snake[j][0] == snake[len(snake) - 1][0]
            and snake[j][1] == snake[len(snake) - 1][1]
        ):
            exit()


### Set Up ###

pygame.init()
screen = pygame.display.set_mode([1200, 600])
clock = pygame.time.Clock()
damier()


draw_blue(snake[0][0], snake[0][1])  # dessin du serpent
draw_blue(snake[1][0], snake[1][1])
draw_blue(snake[2][0], snake[2][1])

draw_rouge(fruit_x, fruit_y)

### Main Loop ###

while True:
    handle_event()
    move(direction)
    eat_fruit()
    snake_die()
    wait_for_next_time(FPS)


print(SCORE)
