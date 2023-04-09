import math
import numpy as np
import matplotlib.pyplot as plt

n = 1000

matrix = np.zeros((1000, 1000))

for x in range(1000):
    for y in range(1000):
        x_norm = 4 * math.pi * x / 1000.0
        y_norm = 4 * math.pi * y / 1000.0 
        matrix[x][y] = math.sin(x_norm) + math.cos(y_norm)


plt.contour(matrix, 20)
plt.imshow(matrix)
plt.show()