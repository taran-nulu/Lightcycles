import pygame

from Direction import *
from Lightcycle import *

pygame.font.init()

width, height = 700, 700
win = pygame.display.set_mode((width, height))
pygame.display.set_caption("Tron Lightcycles")

PADDING = 10

FPS = 20
vel = 10

black = (0, 0, 0)
white = (255, 255, 255)
red = (255, 0, 0)
blue = (0, 0, 255)

winner_font = pygame.font.SysFont('comicsans', 100)

def draw_winner(text):
    draw_text = winner_font.render(text, 1, white)
    win.blit(draw_text, (width/2 - draw_text.get_width()/2, height/2 - draw_text.get_height()/2))
    pygame.display.update()
    pygame.time.delay(3000)

def main():
    player1 = Lightcycle(win, black, red, PADDING, PADDING, Direction.RIGHT, pygame.K_w, pygame.K_s, pygame.K_a, pygame.K_d)
    player2 = Lightcycle(win, black, blue, width - Lightcycle.SIZE - PADDING, height - Lightcycle.SIZE - PADDING, Direction.LEFT, pygame.K_UP, pygame.K_DOWN, pygame.K_LEFT, pygame.K_RIGHT)    

    clock = pygame.time.Clock()
    run = True

    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()
        
        keys_pressed = pygame.key.get_pressed()
        player1.handle_key_press(keys_pressed)
        player2.handle_key_press(keys_pressed)

        player1Status = player1.draw()
        player2Status = player2.draw()

        if player1Status != LightcycleStatus.OK and player2Status != LightcycleStatus.OK:
            draw_winner("It's a draw!")
            run = False
        elif player1Status != LightcycleStatus.OK:
            draw_winner("Blue player wins!")
            run = False
        elif player2Status != LightcycleStatus.OK:
            draw_winner("Red player wins!")
            run = False
        
        pygame.display.update()

if __name__ == "__main__":
    main()