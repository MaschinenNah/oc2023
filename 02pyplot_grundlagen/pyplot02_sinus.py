import math
import numpy as np
from matplotlib import pyplot as plt

sinus = [math.sin(x) for x in np.linspace(0, 2*math.pi, 100)]

plt.plot(sinus)
plt.show()