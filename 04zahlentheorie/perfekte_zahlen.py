def echte_teiler(zahl):
    resultat = []
    max_teiler = zahl // 2 + 1
    for teiler in range(1, max_teiler):
        if (zahl % teiler == 0):
            resultat.append(teiler)
    return resultat

def ist_perfekte_zahl(zahl):
    teiler = echte_teiler(zahl)
    return sum(teiler) == zahl

for zahl in range(34000000):
    if (ist_perfekte_zahl(zahl)):
        print(zahl)