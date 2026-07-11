from turtle import Turtle, Screen
from extract_colors import color_list
import random

screen = Screen()
screen.colormode(255)

a = Turtle()
a.shape("turtle")
a.hideturtle()
a.speed(0)
a.penup()
a.goto(-200, -200)
a.pendown()

for i in range(10):
    for j in range(10):
        a.fillcolor(random.choice(color_list))
        a.begin_fill()
        a.circle(10)
        a.end_fill()
        a.penup()
        a.forward(40)
        a.pendown()

    a.penup()
    a.goto(-200,a.ycor()+50)
    a.pendown()

screen.exitonclick()