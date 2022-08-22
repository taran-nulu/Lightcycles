import pygame

from Direction import *
from Lightcycle import *

width, height = 700, 700
win = pygame.display.set_mode((width, height))
pygame.display.set_caption("Tron Lightcycles")

PADDING = 10

FPS = 20
vel = 10

white = (255, 255, 255)
red = (255, 0, 0)
blue = (0, 0, 255)

def main():
    player1 = Lightcycle(win, red, PADDING, PADDING, Direction.RIGHT, pygame.K_w, pygame.K_s, pygame.K_a, pygame.K_d)
    player2 = Lightcycle(win, blue, width - Lightcycle.SIZE - PADDING, height - Lightcycle.SIZE - PADDING, Direction.LEFT, pygame.K_UP, pygame.K_DOWN, pygame.K_LEFT, pygame.K_RIGHT)    

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

        player1.draw()
        player2.draw()
        pygame.display.update()

if __name__ == "__main__":
    main()