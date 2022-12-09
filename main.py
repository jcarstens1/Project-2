import pygame
import random
import os
import pygame_menu
from pygame_menu import Theme


def play_game():
    #Function calls upon the main function
    main()

def show_score(score) -> bool:
    '''
    Function plays losing sound. Displays the final score for
    a total of 3 seconds.
    :param score: Length of the snake minus one. Score of game.
    :return: Bool value that determines the end of game.
    '''
    LOSE_SOUND.play()
    WIN.fill(LIGHT_BLUE)
    final_font = pygame.font.SysFont('8BIT', 50)
    player_score = final_font.render('Your Score: ' + str(score), True, RED)
    WIN.blit(player_score, [WIDTH//3 - 15,HEIGHT//3])
    pygame.display.update()
    pygame.time.delay(3000)
    return False


def handle_snake(snake_direction, snake_head) -> None:
    '''
    Function that handles how the snake moves around the plane.
    :param snake_direction: String that tells program direction.
    :param snake_head: List used to move the head of snake.
    '''
    if snake_direction == 'up':
        snake_head[1] -= 1
    if snake_direction == 'down':
        snake_head[1] += 1
    if snake_direction == 'left':
        snake_head[0] -= 1
    if snake_direction == 'right':
        snake_head[0] += 1


def draw_window(block_size, snake_head, snake_list, fruit_location, score) -> None:
    '''
    Function that creates the game board and snake body
    following head and logic. Also serves
    as the function to display score on screen.
    :param block_size: Int value of blocks used for game grid.
    :param snake_head: List value of head.
    :param snake_list: List value for length of snake.
    :param fruit_location: Randomized location of the fruit.
    :param score: Score of the player.
    '''
    WIN.fill(LIGHT_BLUE)
    for x in range(0, WIDTH, block_size):
        for y in range(0, HEIGHT, block_size):
            rect = pygame.Rect(x, y, block_size, block_size)
            pygame.draw.rect(WIN, GRAY, rect, 1)

    x, y = fruit_location
    rect = pygame.Rect(x * block_size, y * block_size, block_size, block_size)
    pygame.draw.rect(WIN, YELLOW, rect)

    for x in snake_list[1:]:
        rect = pygame.Rect(x[0] * block_size, x[1] * block_size, block_size, block_size)
        pygame.draw.rect(WIN, PURPLE, rect)

    x, y = snake_head
    rect = pygame.Rect(x * block_size, y * block_size, block_size, block_size)
    pygame.draw.rect(WIN, DARK_PURPLE, rect)

    player_score = score_font.render('Your Score: ' + str(score), True, RED)
    WIN.blit(player_score, [10,10])

    pygame.display.update()

def fruit(snake_list) -> list:
    '''
    Function randomizes where fruit will spawn.
    :param snake_list: Location of the snake body
    :return: Randomized location of fruit on board.
    '''
    while True:
        fruit_location = [random.randrange(0, 17), random.randrange(0, 17)]
        if fruit_location in snake_list:
            fruit_location = [random.randrange(0, 17), random.randrange(0, 17)]
        return fruit_location

    

def main():
    #Creates all the necessary variables to run pygame module.
    #Includes the logic for snake head and body.
    block_size = 34
    snake_head = [8, 8]
    snake_list = [[8,8]]
    fruit_location = fruit(snake_list)
    snake_direction = "right"
    clock = pygame.time.Clock()
    run = True
    #Game loop. Runs until run variable is False.
    while run:
        score = len(snake_list) - 1
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            #Catches users input and stores the direction of snake.
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP and snake_direction != "down":
                    snake_direction = "up"
                if event.key == pygame.K_DOWN and snake_direction != "up":
                    snake_direction = "down"
                if event.key == pygame.K_LEFT and snake_direction != "right":
                    snake_direction = "left"
                if event.key == pygame.K_RIGHT and snake_direction != "left":
                    snake_direction = "right"
        '''
        Moves snake and adds length to snake. There are mo check becuase
        the game will end before reaching this point if anything goes wrong. 
        '''
        handle_snake(snake_direction, snake_head)
        snake_list.insert(0, list(snake_head))
        snake_list.pop()

        #Logic for snake running outside the game board or into itself
        if snake_head[0] * block_size >= WIDTH or snake_head[0] * block_size < 0 or snake_head[1] * block_size >= HEIGHT or snake_head[1] * block_size < 0:
            run = show_score(score)

        for coord in snake_list[1:]:
            if snake_head[0] == coord[0] and snake_head[1] == coord[1]:
                run = show_score(score)

        '''
        checks to see if snake_head is in the same location fruit_location
        if the location matches, then a snake_piece is added and fruit is randomized again
        '''
        if (snake_head[0] * block_size == fruit_location[0] * block_size) and (snake_head[1] * block_size == fruit_location[1] * block_size):
            MUNCH_SOUND.play()
            snake_list.append(fruit_location)
            fruit_location = fruit(snake_list)
        
        draw_window(block_size, snake_head, snake_list, fruit_location, score)

#Before all else, intiate Pygame module. 
pygame.init()
#Window logic that game sits inside of.
WIDTH, HEIGHT = 578, 578
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Project 2 - Snake")
FPS = 8

#Set colors for the menu, game, and final screen.
BLACK = (1,1,1)
GRAY = (30, 30, 30)
YELLOW =(149, 156, 34)
RED = (200, 0, 0)
LIGHT_BLUE = (36, 100, 128)
PURPLE = (96, 60, 133)
DARK_PURPLE = (86, 27, 99)
BLUE = (27, 75, 96)

'''
Loading sound into the game. Sometimes this does not work
due to system settings, as found in our testing.
May have to comment out sound variables in order for game to run.
'''
LOSE_SOUND = pygame.mixer.Sound(os.path.join('assets', "bruh.mp3"))
MUNCH_SOUND = pygame.mixer.Sound(os.path.join('assets', "munch.mp3"))

score_font = pygame.font.SysFont('lucidasanstypewriteroblique', 20)

#Theme is from Pygame_menu module. What controls what is seen on start screen.
my_theme = Theme(background_color=LIGHT_BLUE,
    title_bar_style=pygame_menu.widgets.MENUBAR_STYLE_NONE,
    #if you uncomment, there will be a warning thrown, but there will be
    #no gray bar along the top
    title_font=pygame_menu.font.FONT_8BIT,
    title_font_color=DARK_PURPLE,
    title_offset=(round(WIDTH/3),150),
    widget_font=pygame_menu.font.FONT_MUNRO,
    widget_border_color=PURPLE,
    widget_padding=10
)
#Menu from Pygame_menu module that displays the starting menu to the screen.
menu = pygame_menu.Menu(
    height=HEIGHT,
    theme=my_theme,
    title='Snake',
    width=WIDTH
)
#Buttons from Pygame_menu module that are displayed on the starting menu.
menu.add.button('Play', play_game)
menu.add.button('Quit', pygame_menu.events.EXIT)
'''
Runs the menu loop first, then once "start" button is
clicked, the menu loops begins to loop the main function.
'''
if __name__ == '__main__':
    try:
        menu.mainloop(WIN)
    except:
        print("Goodbye")
