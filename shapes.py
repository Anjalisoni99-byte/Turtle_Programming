from turtle import Turtle,Screen
import turtle as t
import random
s=Screen()
t.colormode(255)
def random_color():
    r=random.randint(0, 255)
    g=random.randint(0, 255)
    b=random.randint(0, 255)
    return (r,g,b)
def shape(num_sides):
    """Draws different shapes based on the number of sides"""
    angle=360/num_sides
    for i in range(num_sides):
        t.forward(100)
        t.right(angle)
for i in range(3,11):
    t.color(random_color())
    shape(i)
s.exitonclick()
