

startwert01 = 0.379 - 0.23 * 1j  # True
startwert02 = 0.3790001 - 0.23 * 1j  # False
startwert03 = 0.37900 - 0.23 * 1j  # False
startwert03 = 0.37900020005 - 0.23 * 1j  # False
startwert04 = 0.3790002000500006 - 0.23 * 1j  # False
#print(startwert01)
#print(type(startwert01))

def schritt(wert, startwert):
    ergebnis = wert**2 + startwert
    return ergebnis

def schritte(startwert, wiederholungen):
    wert = startwert
    for i in range(wiederholungen):
        wert = schritt(wert, startwert)
    return abs(wert) < 2
    
print(startwert01)
print(schritte(startwert01, 200))
print(startwert02)
print(schritte(startwert02, 200))
print(startwert03)
print(schritte(startwert03, 200))
print(startwert04)
print(schritte(startwert04, 200))




