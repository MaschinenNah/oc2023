# A) Listen können Werte unterschiedlicher Typen enthalten, sogar weitere Listen:
zeugs = [3.14, 'Sonnenbrille',  [1, 2, 3]]
print(zeugs)
#=> [3.14, 'Sonnenbrille', [1, 2, 3]]

# B) Zudem könnt ihr Elemente anhängen und entfernen:
zeugs.append('Buch')
print(zeugs)
#=> [3.14, 'Sonnenbrille', [1, 2, 3], 'Buch']
zeugs.remove(3.14)
print(zeugs)
#=> ['Sonnenbrille', [1, 2, 3], 'Buch']

# In vielen Fällen ist das praktisch. Wenn es aber darum geht, Programme zu
# schreiben, die mit großen Datenmengen hantieren, ist diese Flexibilität
# ein Nachteil. Der Prozessor kann VIEL schneller mit Listen arbeiten,
# die eine feste Länge haben und nur Werte gleichen Typs enthalten.
# Genau solche Listen stellt das Package numpy bereit. Wir nennen diese Listen
# Numpy Arrays und sprechen im folgenden kurz von Arrays.

# C) Zunächst müssen wir numpy importieren:
import numpy as np
# Es gibt unzählige Möglichkeiten, ein Array zu erzeugen.
# Wir können hier nur ein paar zeigen.
# Sehr nützlich ist linspace(start, ende, n). Es liefert ein Array mit Werten
# von start bis ende in n Schritten:
von0bis1 = np.linspace(0, 1, 5)
print(von0bis1)
#=> [0.   0.25 0.5  0.75 1.  ]

# D) zeros liefert ein mit Nullen gefülltes Array:
zehnNullen = np.zeros(10)
print(zehnNullen)
#=> [0. 0. 0. 0. 0. 0. 0. 0. 0. 0.]

# E) Arrays können beliebige Dimensionen haben.
# Die letzten beiden Beispiele haben eindimensionale Arrays gezeigt.
# So bekommt ihr ein zweidimensionales Array:
dreiMalDreiNullen = np.zeros((3, 3))
print(dreiMalDreiNullen)
"""
[[0. 0. 0.]
 [0. 0. 0.]
 [0. 0. 0.]]
"""

# F) Das (3, 3) ist die shape (Form) eines Arrays. Ihr könnt sie auch abfragen:
print(dreiMalDreiNullen.shape)
#=> (3, 3)

# G) Der Datentyp eines Arrays ist, wenn nicht anders bestimmt, float64.
# Das bedeutet: Das Array enthält Fließkommazahlen, die jeweils 64 Bit Speicher verbrauchen.
print(dreiMalDreiNullen.dtype)
#=> float64

# H) Ihr könnt bei der Erzeugung eines Arrays einen anderen Datentyp angeben.
# int8 bedeutet: Ganze Zahlen, die jeweils 8 Bit Speicher verbrauchen:
dreiMalDreiNullen = np.zeros((3, 3), np.int8)
print(dreiMalDreiNullen)
"""
[[0 0 0]
 [0 0 0]
 [0 0 0]]
"""
print(dreiMalDreiNullen.dtype)
#=> int8

# I)
zufall = np.random.randint(0, 10, (3, 3), np.int8)
print(zufall)

# test!