import pygame
import random

pygame.init()

WIDTH, HEIGHT = 578, 578
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Project 2 - Snake")
FPS = 9
GRAY = (100, 100, 100)
BLACK = (0, 0, 0)
RED = (200, 0, 0)


def handle_snake(snake_direction, snake_head):
    if snake_direction == 'up':
        snake_head[1] -= 1
    if snake_direction == 'down':
        snake_head[1] += 1
    if snake_direction == 'left':
        snake_head[0] -= 1
    if snake_direction == 'right':
        snake_head[0] += 1


def draw_window(block_size, snake_head, snake_list, fruit_location):
    WIN.fill(GRAY)
    for x in range(0, WIDTH, block_size):
        for y in range(0, HEIGHT, block_size):
            rect = pygame.Rect(x, y, block_size, block_size)
            pygame.draw.rect(WIN, BLACK, rect, 1)

    x, y = fruit_location
    rect = pygame.Rect(x * block_size, y * block_size, block_size, block_size)
    pygame.draw.rect(WIN, RED, rect)

    for x in snake_list:
        rect = pygame.Rect(x[0] * block_size, x[1] * block_size, block_size, block_size)
        pygame.draw.rect(WIN, BLACK, rect)

    x, y = snake_head
    rect = pygame.Rect(x * block_size, y * block_size, block_size, block_size)
    pygame.draw.rect(WIN, BLACK, rect)

    pygame.display.update()

def fruit(snake_list):
    while True:
        fruit_location = [random.randrange(0, 17), random.randrange(0, 17)]
        if fruit_location in snake_list:
            fruit_location = [random.randrange(0, 17), random.randrange(0, 17)]
        return fruit_location

def main():
    block_size = 34
    snake_head = [8, 8]
    snake_list = [[8, 8], [7, 8], [7, 8]]
    fruit_location = fruit(snake_list)
    snake_direction = "right"
    clock = pygame.time.Clock()
    run = True
    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP and snake_direction != "down":
                    snake_direction = "up"
                if event.key == pygame.K_DOWN and snake_direction != "up":
                    snake_direction = "down"
                if event.key == pygame.K_LEFT and snake_direction != "right":
                    snake_direction = "left"
                if event.key == pygame.K_RIGHT and snake_direction != "left":
                    snake_direction = "right"

        if snake_head[0] * block_size >= WIDTH:
            run = False
        if snake_head[0] * block_size < 0:
            run = False
        if snake_head[1] * block_size >= HEIGHT:
            run = False
        if snake_head[1] * block_size < 0:
            run = False

        handle_snake(snake_direction, snake_head)
        snake_list.insert(0, list(snake_head))
        snake_list.pop()

        #checks to see if snake_head is in the same location fruit_location
        #if the location matches, then a snake_piece is added and fruit is randomized again
        if (snake_head[0] * block_size == fruit_location[0] * block_size) and (snake_head[1] * block_size == fruit_location[1] * block_size):
            snake_list.append(fruit_location)
            fruit_location = fruit(snake_list)

        draw_window(block_size, snake_head, snake_list, fruit_location)


if __name__ == '__main__':
    main()
