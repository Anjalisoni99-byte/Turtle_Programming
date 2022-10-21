from turtle import Screen
import turtle as t
import random

s=Screen()
t.width(5)
t.speed("normal")
t.colormode(255)

def random_color():
    r=random.randint(0, 255)
    g=random.randint(0, 255)
    b=random.randint(0, 255)
    return (r,g,b)

directions=[0,90,180,270,360]
for _ in range(50):
        t.color(random_color())
        t.forward(50)
        t.setheading(random.choice(directions))
    
s.exitonclick()
