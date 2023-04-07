#07_pythagoras_baum.py
import math as math
from turtle import *
#Quadrat zeichnen
def quadrat(a):
    p.color('green')
    p.begin_fill()
    for _ in range(4):
        p.forward(a)
        p.right(90)
    p.end_fill()
#Baum zeichnen        
def baum(c,alpha,n):
    a=c*math.cos(math.radians(90-alpha))
    b=c*math.cos(math.radians(alpha))
    quadrat(c)
    if n==0:
        return
    else:
        p.forward(c)
        p.left(alpha)
        baum(b,alpha,n-1)
        p.right(90)
        p.forward(b)
        baum(a,alpha,n-1)
        p.forward(-b)
        p.left(90-alpha)
        p.forward(-c)
#Hauptprogramm       
n=7
winkel=30
c0=80
wn = Screen()
wn.bgcolor('white')
wn.setup(width = 640, height = 480)
wn.title("Pythagoras-Baum")
wn.tracer(False)
p = Turtle()
p.pencolor('green')
p.speed(1)
p.penup()
p.setpos(-40,-180)
p.pendown()
p.setheading(90)
baum(c0,winkel,n) #Funktionsaufruf
wn.update()
wn.mainloop()
