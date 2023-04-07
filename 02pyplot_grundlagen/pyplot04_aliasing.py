import math
import numpy as np
from matplotlib import pyplot as plt

frequenz = 10
n_abtastungen01 = 100
n_abtastungen02 = 7

x = np.linspace(0, math.pi, n_abtastungen01)
y = [math.sin(frequenz*x_) for x_ in x]
x2 = np.linspace(0, math.pi, n_abtastungen02)
y2 = [math.sin(frequenz*x_) for x_ in x2]

# blau:
plt.plot(x, y)
# rot:
plt.plot(x2, y2)
plt.show()