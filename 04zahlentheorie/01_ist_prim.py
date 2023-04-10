import math
import time

# Eine Funktion, die prüft, ob eine Zahl prim ist:
def ist_prim(zahl):
    
    max_teiler = math.floor(math.sqrt(zahl))
    
    for teiler in range(2, max_teiler+1):
        if zahl % teiler == 0:
            # zahl durch teiler ohne Rest teilbar, also keine Primzahl
            return False
    # Diese Zeile wird nur erreicht, wenn alle möglichen Teiler probiert wurden,
    # und keiner gepasst hat:
    return True            
t1 = time.time()
primzahlen = [zahl for zahl in range(2, 1000000) if ist_prim(zahl)]
t2 = time.time()
print("dauer:", t2-t1)
print("anzahl primzahlen:", len(primzahlen))