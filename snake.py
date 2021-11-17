import random
import pygame
from eat import eat
from function import pauseend
pygame.init()
white = (255, 255, 255)
green = (37, 206, 48)
class snake:

    def __init__(self, screen, h, w):
        """Wegen von Richtungsänderung z.B. Z. 39 muss self.size sauber durch Geschwindigkeit teilbar sein"""
        self.speed = 2
        self.size = 50
        self.length = 1
        self.direction = 1  # dann eben 1, 2, 3, 4
        self.nextDirection = 1
        self.x = 50
        self.y = 50
        self.xbef = self.x
        self.ybef = self.y
        self.screen = screen
        self.h = h
        self.w = w

    def draw(self):
        pygame.draw.rect(self.screen, green, (self.x, self.y, self.size, self.size))

    def steuerung(self):
        pressed = pygame.key.get_pressed()
        """Bewgegungsrichtung festlegen"""
        if pressed[pygame.K_RIGHT]:
            self.nextDirection = 1
        elif pressed[pygame.K_UP]:
            self.nextDirection = 2
        elif pressed[pygame.K_LEFT]:
            self.nextDirection = 3
        elif pressed[pygame.K_DOWN]:
            self.nextDirection = 4
        if self.x % self.size == 0 and self.y % self.size == 0:
            self.direction = self.nextDirection

    def bewgung(self):
        self.steuerung()
        """1 = nach rechts
           2 = nach oben
           3 = nach links
           4 = nach unten"""
        self.xbef = self.x
        self.ybef = self.y
        if self.direction == 1:
            self.x = self.x + self.speed
        elif self.direction == 2:
            self.y = self.y - self.speed
        elif self.direction == 3:
            self.x = self.x - self.speed
        elif self.direction == 4:
            self.y = self.y + self.speed

        """Machen, dass Snake nicht aus Bildschirm raus kann, und end vom Spiel"""
        if self.x > self.w - self.size:
            self.x = self.w - self.size
            self.end()
        elif self.x < 0:
            self.x = 0
            self.end()

        if self.y > self.h - self.size:
            self.y = self.h - self.size
            self.end()

        elif self.y < 0:
            self.y = 0
            self.end()


    def eat(self, eatl, tailPiece):
        for eat1 in eatl:
            if eat1.x == self.x and eat1.y == self.y:
                eatl.pop(eatl.index(eat1))
                eatl.append(eat(self.screen, self.h, self.w))
                self.length = self.length + 1
                """directionlast = richtung des letzten schwantzstücks"""
                directionlast = tailPiece[-1].direction
                """x, y werte des letzten stücks um neue koordinaten fest zu legen"""
                if directionlast == 1:
                    neuX = tailPiece[-1].x - tailPiece[-1].size
                    neuY = tailPiece[-1].y
                elif directionlast == 2:
                    neuX = tailPiece[-1].x
                    neuY = tailPiece[-1].y + tailPiece[-1].size
                elif directionlast == 3:
                    neuX = tailPiece[-1].x + tailPiece[-1].size
                    neuY = tailPiece[-1].y
                elif directionlast == 4:
                    neuX = tailPiece[-1].x
                    neuY = tailPiece[-1].y - tailPiece[-1].size
                tailPiece.append(tail(self.screen, self.h, self.w, neuX, neuY, directionlast))
    def hit(self, tailPiece):
        for piece in tailPiece:
            if tailPiece.index(piece) == 0 or tailPiece.index(piece) == 1:
                pass
            else:
                if piece.x == self.x and piece.y == self.y or self.x > piece.x and self.x < (piece.x + self.size) and self.y > piece.y and self.y < (piece.y + self.size):
                    self.end()
    def end(self):
        pauseend(self.screen, self.length, self.w, self.h)

    def all(self, eatl, tailPiece):
        self.bewgung()
        self.steuerung()
        self.eat(eatl, tailPiece)
        self.hit(tailPiece)
        self.draw()

class tail:
    def __init__(self, screen, h, w, x, y, directionlast):
        self.speed = 2
        self.size = 50
        self.direction = directionlast  # dann eben 1, 2, 3, 4
        self.nextDirection = directionlast
        self.x = x
        self.y = y
        self.screen = screen
        self.h = h
        self.w = w

    def bewegung2(self, tailPiece, snakedirection):
        if tailPiece.index(self) == 0:

            if ((self.x + self.speed) % self.size) == 0 and self.y % self.size == 0:
                self.direction = self.nextDirection
            elif self.x % self.size == 0 and ((self.y + self.speed) % self.size) == 0:
                self.direction = self.nextDirection
            self.nextDirection = snakedirection
            if self.direction == 1:
                self.x = self.x + self.speed
            elif self.direction == 2:
                self.y = self.y - self.speed
            elif self.direction == 3:
                self.x = self.x - self.speed
            elif self.direction == 4:
                self.y = self.y + self.speed
        else:
            try:
                if ((self.x + self.speed) % self.size) == 0 and self.y % self.size == 0:
                    self.direction = self.nextDirection
                elif self.x % self.size == 0 and ((self.y + self.speed) % self.size) == 0:
                    self.direction = self.nextDirection
                self.nextDirection = tailPiece[tailPiece.index(self) - 1].direction

                if self.direction == 1:
                    self.x = self.x + self.speed
                elif self.direction == 2:
                    self.y = self.y - self.speed
                elif self.direction == 3:
                    self.x = self.x - self.speed
                elif self.direction == 4:
                    self.y = self.y + self.speed
            except:
                pass

    def draw(self):
        pygame.draw.rect(self.screen, green, (self.x + self.speed, self.y, self.size, self.size))

    def all(self, tailPiece,snakedirection):
        self.bewegung2(tailPiece, snakedirection)
        self.draw()


