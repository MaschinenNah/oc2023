import math

def primzahlen(bis):
    max_faktor = math.ceil(math.sqrt(bis))
    ergebnis = []
    gestrichen = [False] * bis
    
    for i in range(2, max_faktor+1):
        if not gestrichen[i]:
            for j in range(i*2, bis, i):
                gestrichen[j] = True
            
    for i in range(2, bis):
        if not gestrichen[i]:
            ergebnis.append(i)
    return ergebnis


def primfaktoren(zahl):
    ergebnis = []
    rest = zahl
    kandidaten = primzahlen(math.ceil(math.sqrt(zahl))+1)
    kandidat = kandidaten.pop(0)
    
    while(True):
        print("rest:", rest)
        print("kandidat:", kandidat)
        if (rest % kandidat == 0):
            print(kandidat, "ist Teiler von", zahl)
            ergebnis.append(kandidat)
            rest = rest // kandidat
        else:
            kandidat = kandidaten.pop(0)
            print(kandidat, "ist kein Teiler von", zahl)
        if len(kandidaten) == 0:
            break
        
    return ergebnis
        
print(primfaktoren(100))

