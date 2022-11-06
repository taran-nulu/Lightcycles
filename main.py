import pygame

from Direction import *
from Lightcycle import *
from Scorekeeper import *

pygame.font.init()

width, height = 700, 700
scoreboard_height = 50
arena_height = height - scoreboard_height

window = pygame.display.set_mode((width, height))
pygame.display.set_caption("Tron Lightcycles")

scoreboard = window.subsurface(pygame.Rect(0, 0, width, scoreboard_height))
arena = window.subsurface(pygame.Rect(0, scoreboard_height, width, arena_height))

PADDING = 10

FPS = 20
vel = 10

black = (0, 0, 0)
white = (255, 255, 255)
red = (255, 0, 0)
blue = (0, 0, 255)

def main():
    arena.fill(black)

    scorekeeper = Scorekeeper(scoreboard, white, "Red", red, "Blue", blue)

    player1 = Lightcycle(arena, black, red, PADDING, PADDING, Direction.RIGHT, pygame.K_w, pygame.K_s, pygame.K_a, pygame.K_d)
    player2 = Lightcycle(arena, black, blue, width - Lightcycle.SIZE - PADDING, arena_height - Lightcycle.SIZE - PADDING, Direction.LEFT, pygame.K_UP, pygame.K_DOWN, pygame.K_LEFT, pygame.K_RIGHT)

    while True:
        runGame(scorekeeper, player1, player2)

def runGame(scorekeeper, player1, player2):
    clock = pygame.time.Clock()
    run = True

    player1.setPosition(PADDING, PADDING, Direction.RIGHT)
    player2.setPosition(width - Lightcycle.SIZE - PADDING, arena_height - Lightcycle.SIZE - PADDING, Direction.LEFT)
    arena.fill(black)

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
            scorekeeper.updateWinner(0)
            scorekeeper.renderScore()
            run = False
        elif player2Status != LightcycleStatus.OK:
            scorekeeper.updateWinner(1)
            scorekeeper.renderScore()
            run = False
        elif player1Status != LightcycleStatus.OK:
            scorekeeper.updateWinner(2)
            scorekeeper.renderScore()
            run = False

        pygame.display.update()

if __name__ == "__main__":
    main()