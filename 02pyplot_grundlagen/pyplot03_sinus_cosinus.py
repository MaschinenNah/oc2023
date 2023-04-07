import math
import numpy as np
from matplotlib import pyplot as plt

fig, ax = plt.subplots(figsize=(8, 8))

n = 10

sinus = [math.sin(x) for x in np.linspace(0, 2*math.pi, n)]
cosinus = [math.cos(x) for x in np.linspace(0, 2*math.pi, n)]

plt.plot(sinus, cosinus)
plt.show()