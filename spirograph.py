from turtle import Screen
import turtle as t
import random

t.colormode(255)
s=Screen()
directions=[0,90,180,270,360]
t.speed("fastest")

def random_color():
    r=random.randint(0, 255)
    g=random.randint(0, 255)
    b=random.randint(0, 255)
    return (r,g,b)

def draw_spiro(size):
    for _ in range(int(360/size)):
            t.color(random_color())
            t.circle(100)
            t.setheading(t.heading() + size)

draw_spiro(5)      
s.exitonclick()
