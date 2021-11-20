# Import all board pins.
import time
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
x = 0
y = 0

matrix[y, x] = 2
