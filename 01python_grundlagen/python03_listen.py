# Listen und Schleifen

# A) Eine Liste speichert Werte in einer festgelegten Reihenfolge:
aufgaben = ['Einkaufen', 'Kuchen backen', 'Mathe lernen']
print(aufgaben)
#=> ['Einkaufen', 'Kuchen backen', 'Mathe lernen']
print(len(aufgaben))
#=> 3
print(aufgaben[0])
#=> Einkaufen
print(aufgaben[1])
#=> Kuchen backen
print(aufgaben[2])
#=> Mathe lernen
aufgaben.append('Programmieren')
print(aufgaben)
#=> ['Einkaufen', 'Kuchen backen', 'Mathe lernen', 'Programmieren']

# B) Listen sind aufzählbar. Das Aufzählen funktioniert zum Beispiel so:
for aufgabe in aufgaben:
    print('Ich muss noch ' + aufgabe + '!')
#=> Ich muss noch Einkaufen!
#=> Ich muss noch Kuchen backen!
#=> Ich muss noch Mathe lernen!
    
# C) Hier zeigen wir einen eleganten Weg, um aus einer vorhandenen Liste
# eine neue zu erzeugen. Diese Technik nennt sich Listenabstraktion:
zahlen = [1, 3, 5, 7, 11]
mal10 = [zahl * 10 for zahl in zahlen]
print(mal10)
#=> [10, 30, 50, 70, 110]

# D) Wenn Du ganze Zahlen aufzählen willst, kannst Du auch die Funktion range verwenden:
zahlen = range(10)
mal100 = [zahl * 100 for zahl in zahlen]
print(mal100)
#=> [0, 100, 200, 300, 400, 500, 600, 700, 800, 900]

# E) Du kannst bei range() auch einen Startpunkt angeben.
# Und übrigens per list() direkt in eine Liste umwandeln:
von7bis13 = list(range(7, 14))
print(von7bis13)
#=> [7, 8, 9, 10, 11, 12, 13]

# F) Ein drittes Argument bestimmt die Schrittweite:
vielfacheVon7 = list(range(7, 71, 7))
print(vielfacheVon7)
#=> [7, 14, 21, 28, 35, 42, 49, 56, 63, 70]