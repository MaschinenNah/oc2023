#05_spierpinski.py
from turtle import  *

def sierpinski(a,ai):
    if a >= ai:
        for i in range(3):
            p.forward(a)
            p.left(120)
            sierpinski(a/2,ai) #Rekursion
    else:
        return

wn = Screen()
wn.bgcolor("white")
wn.setup(width = 640, height = 480)
wn.title("Sierpinski-Dreieck")
p = Turtle()
p.pencolor("red")
p.pensize(2)
m=6  #Stufe
a0=400
ai=a0/2**m
p.penup()
p.setpos(-200,-180)
p.pendown()
wn.tracer(False)
sierpinski(a0,ai)
wn.update()
print("Stufe:",m,", Anzahl der Dreiecke:",(3**(m+1)-1)/2)
wn.mainloop()
