import pygame
pygame.init()
white = (255, 255, 255)


class score:
    def __init__(self, screen, font):
        self.screen = screen
        self.font = font
        self.length = 1


    def draw(self, length):
        score = self.font.render(str(length), 1, white)
        self.screen.blit(score, (30, 30))

class scoreEnd:
    def __init__(self, screen, fontEnd):
        self.screen = screen
        self.font = fontEnd

    def draw(self, length, w, h):
        endScore = self.font.render("Endscore:" + str(length), 1, white)
        self.screen.blit(endScore, ((w / 2) - (w / 3), (h / 2)))
        pygame.display.flip()
