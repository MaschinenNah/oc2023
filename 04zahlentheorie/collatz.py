def collatz_naiv(zahl):
    zaehler = 0
    while(True):
        if (zahl == 1):
            return zaehler
        
        zaehler = zaehler + 1
        
        if zahl % 2 == 0:
            zahl = zahl / 2
        else:
            zahl = zahl * 3 + 1
            
print([collatz_naiv(zahl) for zahl in range(1, 1000)])


