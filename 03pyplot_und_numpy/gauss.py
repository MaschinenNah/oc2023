import math
import numpy as np
import matplotlib.pyplot as plt
import random

seitenlaenge = 100
wiederholungen = 10000
abweichung = 10

bild = np.zeros((seitenlaenge, seitenlaenge))

for _ in range(5000):
    x = int(random.gauss(seitenlaenge/2, abweichung))
    y = int(random.gauss(seitenlaenge/2, abweichung))
    bild[x%seitenlaenge][y%seitenlaenge] = 1
    
plt.imshow(bild)
plt.show()

