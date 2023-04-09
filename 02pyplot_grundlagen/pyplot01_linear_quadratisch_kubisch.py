# PyPlot ist ein Python Packages zur grafischen Darstellung
# Hier ist ein einfaches Anwendungsbeispiel.

# Du solltest PyPlot immer auf diese Weise importieren:
from matplotlib import pyplot as plt

# Anzahl der Werte, die berechnet und dargestellt werden sollen:
n = 10

# Drei Zahlenfolgen, erzeugt per Listenabstraktion:
ganze_zahlen  = [x for x in range(n)]
quadratzahlen = [x*x for x in range(n)]
kubikzahlen   = [x**3 for x in range(n)]

print(ganze_zahlen)
print(quadratzahlen)
print(kubikzahlen)


# Darstellung der Zahlenfolgen mit PyPlot als Kurve:
plt.plot(ganze_zahlen)
plt.plot(quadratzahlen)
plt.plot(kubikzahlen)
plt.show()

# ... Als Punkte:
plt.plot(ganze_zahlen, '+')
plt.plot(quadratzahlen, '*')
plt.plot(kubikzahlen, 'x')
plt.show()

# ... In ausgewählten Farben
plt.plot(ganze_zahlen, color="purple")
plt.plot(quadratzahlen, color="red")
plt.plot(kubikzahlen, color="lime")
plt.show()

