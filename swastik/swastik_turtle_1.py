from turtle import Turtle, Screen

screen = Screen()
screen.bgcolor("black")

def make_turtle():
    t = Turtle()
    t.hideturtle()
    t.color("red")
    t.speed(1)
    return t

a, b, c, d = make_turtle(), make_turtle(), make_turtle(), make_turtle()
e, f, g, h = make_turtle(), make_turtle(), make_turtle(), make_turtle()

def a_turtle():
    a.left(90)
    a.forward(100)
    a.left(90)
    a.forward(100)
    a.right(45)
    a.forward(20)

def b_turtle():
    b.right(90)
    b.forward(100)
    b.left(90)
    b.forward(100)
    b.right(45)
    b.forward(20)

def c_turtle():
    c.forward(100)
    c.left(90)
    c.forward(100)
    c.right(45)
    c.forward(20)

def d_turtle():
    d.backward(100)
    d.right(90)
    d.forward(100)
    d.right(45)
    d.forward(20)

def e_turtle():
    e.penup()
    e.goto(-50, 50)     # a ke quadrant ka mid-point
    e.pendown()
    e.fillcolor("red")
    e.begin_fill()
    e.circle(10)
    e.end_fill()

def f_turtle():
    f.penup()
    f.goto(50, -50)     # b ke quadrant ka mid-point
    f.pendown()
    f.fillcolor("red")
    f.begin_fill()
    f.circle(10)
    f.end_fill()

def g_turtle():
    g.penup()
    g.goto(50, 50)      # c ke quadrant ka mid-point
    g.pendown()
    g.fillcolor("red")
    g.begin_fill()
    g.circle(10)
    g.end_fill()

def h_turtle():
    h.penup()
    h.goto(-50, -50)    # d ke quadrant ka mid-point
    h.pendown()
    h.fillcolor("red")
    h.begin_fill()
    h.circle(10)
    h.end_fill()

a_turtle()
b_turtle()
c_turtle()
d_turtle()
e_turtle()
f_turtle()
g_turtle()
h_turtle()

screen.exitonclick()

