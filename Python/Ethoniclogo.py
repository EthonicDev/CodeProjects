import turtle
import random
import time


turtle.speed(0)
turtle.bgcolor("black")

turtle.fillcolor("orange")
turtle.color("orange")
turtle.begin_fill()

turtle.goto(0, 100)
turtle.goto(-50, 50)
turtle.goto(-50, 0)
turtle.goto(0, 0)

turtle.end_fill()
turtle.fillcolor("#00bfff")
turtle.color("#00bfff")
turtle.begin_fill()

turtle.goto(-50, 0)
turtle.goto(0, -50)
turtle.goto(50, -50)
turtle.goto(50, 0)
turtle.goto(-50, 0)

turtle.end_fill()
turtle.goto(50, -50)

turtle.fillcolor("orange")
turtle.color("orange")
turtle.begin_fill()
turtle.goto(50, 50)
turtle.goto(100, 50)
turtle.goto(100, 0)
turtle.goto(50, -50)
turtle.end_fill()
turtle.goto(100, 50)

turtle.fillcolor("#00bfff")
turtle.color("#00bfff")
turtle.begin_fill()
turtle.goto(0, 150)
turtle.goto(0, 100)
turtle.goto(50, 50)
turtle.goto(100, 50)

turtle.end_fill()
turtle.penup

turtle.pendown






turtle.exitonclick()