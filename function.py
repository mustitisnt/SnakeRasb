import pygame
from score import scoreEnd
pygame.init()

def pause():

    while True:
        pressed = pygame.key.get_pressed()
        event = pygame.event.get()
        if pressed[pygame.K_SPACE]:
            break
        for key in event:
            if key.type == pygame.QUIT:
                pygame.quit()
                quit()
                exit()

def pauseend(screen, length, w, h):
    fontend = pygame.font.SysFont("Arial", 90, True)
    score2 = scoreEnd(screen, fontend)
    while True:
        score2.draw(length, w, h)
        event = pygame.event.get()
        for key in event:
            if key.type == pygame.QUIT:
                pygame.quit()
                quit()
                exit()



