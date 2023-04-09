import math

# Eine Funktion, die prüft, ob eine Zahl prim ist:
def ist_prim(zahl):
    
    max_teiler = math.ceil(math.sqrt(zahl))
    
    for teiler in range(2, max_teiler+1):
        if zahl % teiler == 0:
            # zahl durch teiler ohne Rest teilbar, also keine Primzahl
            return False
    # Diese Zeile wird nur erreicht, wenn alle möglichen Teiler probiert wurden,
    # und keiner gepasst hat:
    return True            


for zahl in range(100):
    if ist_prim(zahl):
        print(zahl)