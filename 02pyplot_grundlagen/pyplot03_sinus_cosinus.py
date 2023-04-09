import math
import numpy as np
from matplotlib import pyplot as plt

fig, ax = plt.subplots(figsize=(8, 8))

n = 500

# Kreis:
sinus =   [math.sin(x) for x in np.linspace(0, 2*math.pi, n)]
cosinus = [math.cos(x) for x in np.linspace(0, 2*math.pi, n)]

# Spirale:
# sinus =   [x * math.sin(x) for x in np.linspace(0, 8 * 2*math.pi, n)]
# cosinus = [x * math.cos(x) for x in np.linspace(0, 8 * 2*math.pi, n)]

plt.plot(sinus, cosinus, linewidth=10, color='r')
plt.show()