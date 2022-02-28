from turtle import Turtle, colormode, done
leo: Turtle = Turtle()

leo.penup()
leo.goto(45, 60)
leo.pendown()

i: int = 0
while (i < 4):
    leo.forward(300)
    leo.left(120)
    i = i + 1  

leo.begin_fill()
colormode(255) 
leo.end_fill()

bob: Turtle = Turtle()
bob.pencolor("blue")
side_length: int = 300

i: int = 0
while (i < 3):
    bob.forward(side_length)
    bob.left(120)
    i = i + 1 

i: int = 0
while(i < 3):
    bob.forward(300)
    bob.left(120)
    i = i + 1
    side_length = side_length * 120 
done()