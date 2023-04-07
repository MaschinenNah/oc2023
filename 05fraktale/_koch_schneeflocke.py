#03_koch_schneeflocke.py
import time, random
from turtle import  *


def koch(a, n):
    global m
    winkel01 = 70
    winkel02 = 50
    if n>0:
        for phi in [0, winkel01, -120, winkel02]:
            p.left(phi)
            koch(a/3,n-1) #Rekursion
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
p.pencolor("red")
p.pensize(1)
p.penup()
p.setpos(-200,100)
p.pendown()
p.speed(1)
m = 3   #Entwicklungsstufe
a0=400
wn.tracer(False)
koch(a0, m)
p.right(120)
koch(a0, m)
p.right(120)
koch(a0, m)
wn.update()
wn.mainloop()

