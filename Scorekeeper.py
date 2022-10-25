import pygame

pygame.font.init()

SCORE_WIDTH = 700
SCORE_HEIGHT = 0
SCORE_FONT = pygame.font.SysFont('comicsans', 30)

black = (0, 0, 0)

class Scorekeeper:
    def __init__(self, surface, surfaceColor, player1Name, player1Color, player2Name, player2Color):
        self.surface = surface
        self.surfaceColor = surfaceColor
        self.player1Name = player1Name
        self.player1Color = player1Color
        self.player2Name = player2Name
        self.player2Color = player2Color
        self.player1Score = 0
        self.player2Score = 0

        self.surface.fill(self.surfaceColor)

    def updateWinner(self, playerNumber):
        if playerNumber == 0:
            drawText = SCORE_FONT.render("It is a Draw!", 1, black)
        elif playerNumber == 1:
            self.player1Score += 1
            drawText = SCORE_FONT.render(f"{self.player1Name} Wins!", 1, self.player1Color)
        elif playerNumber == 2:
            self.player2Score += 2
            drawText = SCORE_FONT.render(f"{self.player2Name} Wins!", 1, self.player2Color)
        self.surface.blit(drawText, (SCORE_WIDTH/2 - drawText.get_width()/2, SCORE_HEIGHT))
        pygame.display.update()
        pygame.time.delay(3000)
        self.surface.fill(self.surfaceColor)
        