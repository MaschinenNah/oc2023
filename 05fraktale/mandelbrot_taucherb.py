import numpy as np
import matplotlib.pyplot as plt
import math

np.seterr(all="ignore")

fig, ax = plt.subplots(figsize=(8, 8))

# Aufloesung des dargestellten Ausschnittes
n_pixel = 800

# Durchmesser des untersuchten Ausschnittes
d = np.array(3, np.longdouble)

# Linke obere Ecke des dargestellten Ausschnittes
x_min = -0.5-d/2
y_min = 0-d/2

# Minimale Anzahl an Iterationen:
min_iterationen = 100

def ausschnitt_berechnen():
    resultat = np.zeros((n_pixel, n_pixel))
    n_iterationen = int(min_iterationen - (math.log(d, 10)*10))
    print("Anzahl Iterationen", n_iterationen)
    n_snapshots = 20
    iterationen_pro_snapshot = int(n_iterationen / n_snapshots)
    
    schrittweite = d / n_pixel;
    print("Auflösung", d)
    
    matrix = np.zeros((n_pixel, n_pixel), np.clongdouble)
    for x in range(n_pixel):
        for y in range(n_pixel):
            matrix[x][y] = (x_min + x*schrittweite) + ((y_min + y*schrittweite) * 1j)
    z = matrix
    
    for snapshot_nummer in range(n_snapshots):
        for _ in range(iterationen_pro_snapshot):
            z = z**2 + matrix
            
        snapshot = (np.abs(z) < 2).T.astype(np.int8) / (snapshot_nummer+1)
        resultat += snapshot
        
    return resultat

def ausschnitt_zeichnen(ausschnitt):
    plt.imshow(ausschnitt)

    plt.show()
    
def pixel_zu_koordinate(x_pixel, y_pixel):
    schrittweite = d / n_pixel;
    x_koord = x_min + x_pixel * schrittweite
    y_koord = y_min + y_pixel * schrittweite
    return x_koord, y_koord
    
def onclick(event):
    global d, x_min, y_min
    x_pixel, y_pixel = event.xdata, event.ydata
    x_koord, y_koord = pixel_zu_koordinate(x_pixel, y_pixel)
    d = d / 5
    x_min = x_koord - d/2
    y_min = y_koord - d/2
    ausschnitt = ausschnitt_berechnen()
    ausschnitt_zeichnen(ausschnitt)

fig.canvas.mpl_connect('button_press_event', onclick)

ausschnitt = ausschnitt_berechnen()
ausschnitt_zeichnen(ausschnitt)