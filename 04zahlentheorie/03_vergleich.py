import time
import math
from primePy import primes

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
        if (rest % kandidat == 0):
            ergebnis.append(kandidat)
            rest = rest // kandidat
        else:
            kandidat = kandidaten.pop(0)
        if len(kandidaten) == 0:
            break
        
    return ergebnis

# Vergleich Primzahlen
print("Primzahlen")
grenze = 100000

t1 = time.time()
primzahlenPrimePy = primes.upto(grenze)
t2 = time.time()
print("primePy:", t2-t1)

t1 = time.time()
primzahlenEigenbau = primzahlen(grenze)
t2 = time.time()
print("Eigenbau:", t2-t1)

for i in range(len(primzahlenPrimePy)):
    if (primzahlenPrimePy[i] != primzahlenEigenbau[i]):
        print("Die Ergebnisse sind nicht gleich!")
        
# Vergleich Primfaktoren
print("Primfaktoren")
zahl = 12345678438949

t1 = time.time()
primfaktorenPrimePy = primes.factors(zahl)
t2 = time.time()
print("primePy:", t2-t1)
print(primfaktorenPrimePy)

t1 = time.time()
primfaktorenEigenbau = primfaktoren(zahl)
t2 = time.time()
print("Eigenbau:", t2-t1)
print(primfaktorenEigenbau)

for i in range(len(primfaktorenPrimePy)):
    if (primfaktorenPrimePy[i] != primfaktorenEigenbau[i]):
        print("Die Ergebnisse sind nicht gleich!")
