# Die arithmetischen Operatoren in Python

# A) Addition
print(3 + 4)
# => 7

# B) Subtraktion
print(21 - 12)
# => 9
print(3 - 7)
# => -4

# C) Multiplikation
print(7 * 8)
# => 56
 
# D) Division
print(10 / 3)
# => 3.3333333333333335
# Das Ergebnis einer Division ist immer eine Dezimalzahl (=Kommazahl), auch wenn sie
# ganzzahlig aufgeht:
print(15 / 5)
# =>  3.0

# E) Potenz
print(2 ** 4)
# => 16
# In Python könnt ihr mit im Prinzip beliebig großen Zahlen rechnen:
print(2 ** 1000) 
# => 10715086071862673209484250490600018105614048117055336074437503883703510511249361224931983788156958581275946729175531468251871452856923140435984577574698574803934567774824230985421074605062371141877954182153046474983581941267398767559165543946077062914571196477686542167660429831652624386837205668069376

# F) Der Modulo Operator % gibt den Rest nach einer ganzzahligen Division
print(10 % 3)
# => 1
# Wenn a % b == 0, dann bedeutet dass, das a durch b teilbar ist:
print(28 % 7)
# => 0
# Prüfung der Teilbarkeit sieht dann so aus:
print(28 % 7 == 0)
# => True

# G) Der Operator für ganzzahlige Division // gibt das
# gerundete Ergebnis einer Division:
print(10 // 3)
# => 3