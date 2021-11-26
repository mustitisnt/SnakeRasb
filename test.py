""""""
import pygame
from snake import snake, tail
from eat import eat
from score import score
from function import pause
import board
import busio
from adafruit_ht16k33 import matrix

# Create the I2C interface.
i2c = busio.I2C(board.SCL, board.SDA)

# creates a 8x8 matrix:
matrix = matrix.Matrix8x8(i2c)

# edges of an 8x8 matrix
col_max = 8
row_max = 8

# Clear the matrix.
matrix.fill(0)
col = 0
row = 0

M = [[0, 0, 0, 0, 0, 0, 0, 0],
     [0, 0, 0, 0, 0, 0, 0, 0],
     [0, 0, 0, 0, 0, 0, 0, 0],
     [0, 0, 0, 0, 0, 0, 0, 0],
     [0, 0, 0, 0, 0, 0, 0, 0],
     [0, 0, 0, 0, 0, 0, 0, 0],
     [0, 0, 0, 0, 0, 0, 0, 0],
     [0, 0, 0, 0, 0, 0, 0, 0]]

pygame.init()
black = (0, 0, 0)
h = 400
w = 400
screen = pygame.display.set_mode((h, w))
pygame.display.set_caption("Snake")
clock = pygame.time.Clock()
snake1 = snake(screen, h, w)
"""Wie viele Dinke zum essen auf Karte existieren ist eatl"""
eatl = []
eatl.append(eat(screen, h, w))
"""Wie viele Schwanzstücke es gibt ist tailPiece"""
tailPiece = []
tailPiece.append(tail(screen,h, w, snake1.x - snake1.size, snake1.y, 1))
font = pygame.font.SysFont("Arial", 30, True)
score1 = score(screen, font)
while True:
    screen.fill(black)
    event = pygame.event.get()
    pressed = pygame.key.get_pressed()
    for key in event:
        if key.type == pygame.QUIT:
            pygame.quit()
            quit()
    if pressed[pygame.K_ESCAPE]:
        pause()
    snake1.all(eatl, tailPiece)
    for piece in tailPiece:
        piece.all(tailPiece, snake1.direction)

    for eat in eatl:
        eat.draw()
        xl = (eat.x/50) - 1
        yl = (eat.y/50) - 1
        """Warscheinlich gibt es verschiebungen mit x und y und so"""

        matrix[yl, xl] = 2

    score1.draw(snake1.length)
    if snake1.x % snake1.size == 0 and snake1.y % snake1.size == 0:
        x = int(snake1.x / 50)
        y = int(snake1.y / 50)
        for piece in tailPiece:
            xp = int(piece.x/50)
            yp = int(piece.y/50)
            if piece.direction == 2:
                xp = x
                yp = yp
            elif piece.direction == 4:
                xp = x
            elif piece.direction == 3:
                xp = xp + 1
            elif piece.direction == 1:
                xp = xp
                yp = yp
            if piece.direction == 1:
                xp = xp + 1
            elif piece.direction == 2:
                yp = yp - 1
            elif piece.direction == 3:
                xp = xp - 1
            elif piece.direction == 4:
                yp = yp + 1
            """Verschiebung der Matrix ausgleichen hoffentlich"""
            if yp == 7:
                yp = 0
            else:
                yp = yp + 1
            try:
                M[yp][xp] = 1
                """Warscheinlich gibt es verschiebungen mit x und y und so"""

                matrix[yp, xp] = 2
            except:
                print("Auserhalb der Reichweite Schwanz")

        if snake1.direction == 2:
            x = x
            y = y - 1
        if snake1.direction == 1:
            x = x + 1
        elif snake1.direction == 2:
            y = y - 1
        elif snake1.direction == 3:
            x = x - 1
        elif snake1.direction == 4:
            y = y + 1
        """Verschiebung der Matrix ausgleichen hoffentlich"""
        if yp == 7:
            yp = 0
        else:
            yp = yp + 1
        try:
            M[y][x] = 1
            """Warscheinlich gibt es verschiebungen mit x und y und so"""
          #  matrix[y, x] = 2
        except:
            print("Auserhalbt der Reichweite der Matrix")
        for i in M:
            print(i, "\n")
        print("\n \n \n \n \n")
        xm = 0
        ym = 0
        for i in M:
            ym = ym + 1
            for j in i:
                xm = xm + 1
                if j == 0:
                    matrix[ym, xm] = 0
        M = [[0, 0, 0, 0, 0, 0, 0, 0],
     [0, 0, 0, 0, 0, 0, 0, 0],
     [0, 0, 0, 0, 0, 0, 0, 0],
     [0, 0, 0, 0, 0, 0, 0, 0],
     [0, 0, 0, 0, 0, 0, 0, 0],
     [0, 0, 0, 0, 0, 0, 0, 0],
     [0, 0, 0, 0, 0, 0, 0, 0],
     [0, 0, 0, 0, 0, 0, 0, 0]]
    """manchmal passt es nicht ganz weil Marix noch nicht passen uberschrieben wurde. sollte hinderher hoffentlich kein Problem darstellen"""

    clock.tick(50) # sollt FPS auf 50 begrenzen
    pygame.display.flip()
