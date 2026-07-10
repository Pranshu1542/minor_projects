from turtle import Turtle, Screen

screen = Screen()
screen.bgcolor("black")

def make_turtle():
    t = Turtle()
    t.hideturtle()
    t.color("red")
    t.speed(1)
    return t

# 4 line-turtles + 4 circle-turtles
turtles = [make_turtle() for _ in range(8)]
a, b, c, d, e, f, g, h = turtles

# har turtle ki movement steps: (function_name, angle) pairs
moves = [
    [(a.left, 90), (a.forward, 100), (a.left, 90), (a.forward, 100), (a.right, 45), (a.forward, 20)],
    [(b.right, 90), (b.forward, 100), (b.left, 90), (b.forward, 100), (b.right, 45), (b.forward, 20)],
    [(c.forward, 100), (c.left, 90), (c.forward, 100), (c.right, 45), (c.forward, 20)],
    [(d.backward, 100), (d.right, 90), (d.forward, 100), (d.right, 45), (d.forward, 20)],
]

for path in moves:
    for func, val in path:
        func(val)

# circle turtles ke quadrant mid-points
circle_data = [(e, -50, 50), (f, 50, -50), (g, 50, 50), (h, -50, -50)]

for t, x, y in circle_data:
    t.penup()
    t.goto(x, y)
    t.pendown()
    t.fillcolor("red")
    t.begin_fill()
    t.circle(10)
    t.end_fill()

screen.exitonclick()
