# Funktionen

# A) Funktionen definiert ihr in Python mit def:
def meine_funktion():
    print("Du hast grad meine Funktion aufgerufen!")
    print("Ich hoffe, das hat Dir Freude bereitet!")
# Die Zeilen 5 und 6 sind der Körper der Funktion, also der
# Code, der bei Aufruf der Funktion ausgeführt wird:
meine_funktion()
#=> Du hast grad meine Funktion aufgerufen!
#=> Ich hoffe, das hat Dir Freude bereitet!

# Der Körper einer Funktion wird in Python immer durch Einrückungen markiert,
# nicht mit geschweiften Klammern (wie z.B. in C, Java, Javascript) oder
# mit do ... end (wie z.B. in Ruby oder Lua)

# B) So baust Du Argumente in Deine Funktionen ein und lieferst Werte zurück:
def mal_drei(zahl):
    return 3 * zahl
# Der Aufruf läuft wie gehabt:
print(mal_drei(10))
#=> 30
print(mal_drei(7))
#=> 21
# Überraschung:
print(mal_drei('hi'))
#=> hihihi
