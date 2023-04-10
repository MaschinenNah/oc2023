import numpy as np
from matplotlib import pyplot as plt
import warnings

warnings.filterwarnings('ignore')

def schritt(wert, startwert):
    ergebnis = wert**2 + startwert
    return ergebnis

def schritte(startwert, wiederholungen):
    wert = startwert
    for _ in range(wiederholungen):
        wert = schritt(wert, startwert)
    if (abs(wert) < 2):
        return '*'
    else:
        return "_"
    
iterationen = 200
aufteilung = 80
    
startwerte01 = np.linspace((0.379 - 0.23 * 1j), (0.380 - 0.23 * 1j),  aufteilung)
startwerte02 = np.linspace((0.379 - 0.23 * 1j), (0.3795 - 0.23 * 1j),  aufteilung)
startwerte03 = np.linspace((0.379 - 0.23 * 1j), (0.37925 - 0.23 * 1j),  aufteilung)
startwerte04 = np.linspace((0.379 - 0.23 * 1j), (0.379125 - 0.23 * 1j),  aufteilung)
startwerte05 = np.linspace((0.379 - 0.23 * 1j), (0.3790625 - 0.23 * 1j),  aufteilung)
startwerte06 = np.linspace((0.379 - 0.23 * 1j), (0.37903125 - 0.23 * 1j),  aufteilung)
startwerte07 = np.linspace((0.379 - 0.23 * 1j), (0.3790306125 - 0.23 * 1j),  aufteilung)

werte = [schritte(startwert, iterationen) for startwert in startwerte01]
werte_als_string = ''.join(werte)
print(werte_als_string)

werte = [schritte(startwert, iterationen) for startwert in startwerte02]
werte_als_string = ''.join(werte)
print(werte_als_string)

werte = [schritte(startwert, iterationen) for startwert in startwerte03]
werte_als_string = ''.join(werte)
print(werte_als_string)

werte = [schritte(startwert, iterationen) for startwert in startwerte04]
werte_als_string = ''.join(werte)
print(werte_als_string)

werte = [schritte(startwert, iterationen) for startwert in startwerte05]
werte_als_string = ''.join(werte)
print(werte_als_string)

werte = [schritte(startwert, iterationen) for startwert in startwerte06]
werte_als_string = ''.join(werte)
print(werte_als_string)

werte = [schritte(startwert, iterationen) for startwert in startwerte07]
werte_als_string = ''.join(werte)
print(werte_als_string)