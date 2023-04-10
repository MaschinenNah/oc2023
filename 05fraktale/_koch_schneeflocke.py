# Bearbeitung eines Beispielprogramms aus
# https://www.rheinwerk-verlag.de/mathematische-algorithmen-mit-python/
import time, random
from turtle import  *


def koch(a, n):
    global m
    winkel01 = 60
    winkel02 = 60
    if n > 0:
        for phi in [0, winkel01, -120, winkel02]:
            p.left(phi)
            koch(a/3,n-1)
            time.sleep(0.1/m)
            wn.update()
    else:
        p.forward(a)
    return
        
wn = Screen()
wn.bgcolor("white")
wn.setup(width = 640, height = 640)
wn.title("Koch-Kurve")
p = Turtle()
p.pencolor("blue")
p.pensize(1)
p.penup()
p.setpos(-200,100)
p.pendown()
p.speed(1)
#Entwicklungsstufe
m = 1   
a0 = 400
wn.tracer(False)
koch(a0, m)
p.right(120)
koch(a0, m)
p.right(120)
koch(a0, m)
wn.update()
wn.mainloop()

