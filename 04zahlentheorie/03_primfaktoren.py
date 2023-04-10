import math

# Baustelle! Funktioniert noch nicht!

def primzahlen(bis):
    max_faktor = math.ceil(math.sqrt(bis))
    ergebnis = []
    gestrichen = [False] * bis
    
    for i in range(2, max_faktor+1):
        #print("starte bei", i)
        if not gestrichen[i]:
            for j in range(i*2, bis, i):
                #print("streiche", j)
                gestrichen[j] = True
        #else:
            #print(i, "ist schon gestrichen")
            
    for i in range(2, bis):
        if not gestrichen[i]:
            ergebnis.append(i)
    return ergebnis


def primfaktoren(zahl):
    ergebnis = []
    rest = zahl
    kandidaten = primzahlen(math.ceil(math.sqrt(zahl))+2)
    print("kandidaten:", kandidaten)
    kandidat = kandidaten.pop(0)

    
    while(True):
        if len(kandidaten) == 0:
            break
        
        print("rest:", rest)
        print("kandidat:", kandidat)
        if (rest % kandidat == 0):
            print(kandidat, "ist Teiler von", zahl)
            ergebnis.append(kandidat)
            rest = rest // kandidat
            
        else:
            kandidat = kandidaten.pop(0)
            print(kandidat, "ist kein Teiler von", zahl)

        
    return ergebnis
        

print(primfaktoren(10))

'''
for n in range(2, 100):
    print("###################")
    print("n:", n)
    faktoren = primfaktoren(n)
    print("faktoren:", faktoren)
'''


