import pygame

WIDTH, HEIGHT = 595, 595
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Project 2 - Snake")
FPS = 60
GRAY = (100, 100, 100)
BLACK = (0, 0, 0)
SNAKE_VEL = 5


# def handle_snake(key_pressed, snake_list):
#     for x in snake_list:
#         pygame.draw.rect(WIN, BLACK, )


def draw_window(snake_list):
    WIN.fill(GRAY)
    block_size = 35
    for x in range(0, WIDTH, block_size):
        for y in range(0, HEIGHT, block_size):
            rect = pygame.Rect(x, y, block_size, block_size)
            pygame.draw.rect(WIN, BLACK, rect, 1)

    x, y = snake_list[0]
    rect = pygame.Rect(x * block_size, y * block_size, block_size, block_size)
    pygame.draw.rect(WIN, BLACK, rect)

    for x, y in snake_list[1:]:
        rect = pygame.Rect(x * block_size, y * block_size, block_size, block_size)
        pygame.draw.rect(WIN, BLACK, rect)

    pygame.display.update()


def main():
    snake_list = [(8, 8), (7, 8), (6, 8)]
    clock = pygame.time.Clock()
    run = True
    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
        key_pressed = pygame.key.get_pressed()
        #handle_snake(key_pressed, snake_list)

        draw_window(snake_list)


if __name__ == '__main__':
    main()
