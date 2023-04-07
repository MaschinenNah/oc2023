def alle_teiler(zahl):
    resultat = []
    max_teiler = zahl // 2 + 1
    for teiler in range(1, max_teiler):
        if (zahl % teiler == 0):
            resultat.append(teiler)
    #resultat.append(zahl)
    return resultat


def hochzusammengesetzte_zahlen(max_zahl):
    resultat = []
    anzahl_teiler = 0
    for zahl in range(1, max_zahl):
        anzahl_teiler_neu = len(alle_teiler(zahl))
        if anzahl_teiler_neu > anzahl_teiler:
            resultat.append(zahl)
            anzahl_teiler = anzahl_teiler_neu
    return resultat

print(hochzusammengesetzte_zahlen(1000))
