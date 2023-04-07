import math

def istPrim(zahl):
    
    max_teiler = math.ceil(math.sqrt(zahl)) + 1
    
    for teiler in range(2, max_teiler):
        if zahl % teiler == 0:        # ohne Rest teilbar
            return zahl, False   # also keine Primzahl
    return zahl, True            # ist eine Primzahl

# Hauptprogramm
ergebnis = [istPrim(z) for z in range(2, 10000)]

print("fertig")