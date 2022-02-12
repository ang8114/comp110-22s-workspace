from turtle import Turtle, colormode, done
leo: Turtle = Turtle()

leo.color("blue")
leo.penup()
leo.goto(45, 60)
leo.pendown()

i: int = 0
while (i < 4):
    leo.forward(300)
    leo.left(120)
    i = i + 1   