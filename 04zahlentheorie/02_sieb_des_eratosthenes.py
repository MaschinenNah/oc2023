import math
import time

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

#Hauptprogramm
t1 = time.time()
p = primzahlen(1000000)
t2 = time.time()
print("dauer:", t2-t1)

print(p)

