# Bezeichner und Typen

# A) So weisen wir einem Bezeichner Werte zu und rechnen mit Bezeichnern:
a = 1
b = 2
c = a + b
print(c)
#=> 3

# B) Anders als in Programmiersprachen wie Java oder C müssen wir dem
# Computer nicht den Typen nennen. Der Computer folgert den Typ automatisch.
# Die Funktion type() liefert den Typ eines Wertes (bzw. den Typ des Wertes,
# auf den ein Bezeichner verweist:
print(type(1))
#=> <class 'int'>
print(type(3.14))
#=> <class 'float'>
print(type('hallo'))
#=> <class 'str'>
print(type([1, 2, 3, 4]))
#=> <class 'list'>

# C) Auch Funktionen sind Werte, und sie haben einen Typ!
print(print)
#=> <built-in function print>
drucken = print
drucken('So geht es auch!')
#=> So geht es auch!