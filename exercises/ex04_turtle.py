"""A simple landscape with trees during a pastel sunset with pink heart clouds.""" 

__author__ = "730391695"


from turtle import Turtle, done, colormode, tracer, update
import turtle
colormode(255)

MAX_SPEED: int = 0


def main() -> None:
    """The entrypoint of my scene."""
    tracer(0, 0)
    paintbrush: Turtle = Turtle()
    paintbrush.speed(MAX_SPEED)
    turtle.Screen().bgcolor("#D1EEEE")
    grass(paintbrush, -400, -100)
    tree(paintbrush, -300, -200)
    tree(paintbrush, -200, -100)
    tree(paintbrush, 100, -175)
    tree(paintbrush, 200, -200)
    tree_leaves(paintbrush, -280, -100)
    tree_leaves(paintbrush, -180, -20)
    tree_leaves(paintbrush, 120, -100)
    tree_leaves(paintbrush, 210, -110)
    apple_body(paintbrush, 220, -230)
    apple_body(paintbrush, -220, -230)
    sun(paintbrush, 296, 285)
    heart_cloud(paintbrush, -200, 180)
    heart_cloud(paintbrush, -50, 180)
    heart_cloud(paintbrush, 70, 185)
    heart_cloud(paintbrush, -300, 200)
    heart_cloud(paintbrush, 220, 160)
    heart_cloud(paintbrush, 230, 162)
    heart_cloud(paintbrush, 170, 220)
    heart_cloud(paintbrush, 0, 270)
    heart_cloud(paintbrush, 5, 10)
    heart_cloud(paintbrush, 200, 40)
    update()
    done()


def cloud(t_cloud: Turtle, x: float, y: float) -> None:
    """Draws light pink filled cirlce which will be repeated to create a full cloud in function heart_cloud."""
    t_cloud.penup()
    t_cloud.goto(x, y)
    t_cloud.pendown()
    t_cloud.pencolor("pink")
    t_cloud.fillcolor("pink")
    t_cloud.speed(100)

    i: int = 0
    t_cloud.begin_fill()
    while i < 1:
        t_cloud.forward(11)
        t_cloud.right(5)
        t_cloud.circle(25.5)
        i = i + 1
    t_cloud.end_fill()


def heart_cloud(cloud_turtle: Turtle, x: float, y: float) -> None:
    """Creates a heart shaped cloud using small, pink filled circles from repeated cloud funtion."""
    i: int = 0
    cloud_turtle.speed(350)
    cloud_turtle.setheading(0.0)
    while i < 50.1:
        cloud(cloud_turtle, x + 10, y + 20)
        i = i + 1


def triangle(tree_top: Turtle, x: float, y: float) -> None:
    """Creates a green triangle which will be repeated in tree function to create leaves of the tree."""
    i: int = 0
    tree_top.penup()
    tree_top.goto(x, y)
    tree_top.pendown()
    tree_top.pencolor(58, 195, 73)
    tree_top.fillcolor(58, 195, 73)
    tree_top.begin_fill()
    while (i < 3):
        tree_top.forward(100)
        tree_top.left(120)
        i = i + 1
    tree_top.end_fill()


def tree_base(base_turtle: Turtle, x: float, y: float) -> None:
    """Creates a brown rectangle which will be the trunk of a tree in function tree."""
    base_turtle.penup()
    base_turtle.goto(x, y)
    base_turtle.pendown()
    base_turtle.pencolor("brown")
    base_turtle.fillcolor("brown")
    base_turtle.begin_fill()

    base_turtle.forward(50)
    base_turtle.right(90)
    base_turtle.forward(40)
    base_turtle.right(90)
    base_turtle.forward(50)
    base_turtle.right(90)
    base_turtle.forward(40)
    base_turtle.right(90)

    base_turtle.end_fill()


def tree(pen: Turtle, x: float, y: float) -> None:
    """Creates a tree with trunk and 3 triangle bodies."""
    pen.speed(350)
    tree_base(pen, x, y)
    triangle(pen, x - 25, y)
    triangle(pen, x - 25, y + 30)
    triangle(pen, x - 25, y + 60)


def sun(sun_turtle: Turtle, x: float, y: float) -> None:
    """Creates the circular body of sun."""
    sun_turtle.penup()
    sun_turtle.goto(x, y)
    sun_turtle.pendown()
    sun_turtle.pencolor(242, 124, 25)
    sun_turtle.fillcolor(242, 124, 25)
    sun_turtle.color((248, 254, 23), (242, 124, 25))

    sun_turtle.begin_fill()
    sun_turtle.circle(60)
    sun_turtle.end_fill()


def grass(grass_turtle: Turtle, x: float, y: float) -> None:
    """Creates a solid body of green grass at the bottom of landscape."""
    grass_turtle.penup()
    grass_turtle.goto(x, y)
    grass_turtle.pendown()
    grass_turtle.pencolor(74, 174, 59)
    grass_turtle.fillcolor(74, 174, 59)
    grass_turtle.begin_fill()

    grass_turtle.forward(748)
    grass_turtle.right(90)
    grass_turtle.forward(300)
    grass_turtle.right(90)
    grass_turtle.forward(748)
    grass_turtle.right(90)
    grass_turtle.forward(300)
    grass_turtle.right(90)

    grass_turtle.end_fill()


def tree_details(details_turtle: Turtle, x: float, y: float) -> None:
    """Creates v shaped points that will be repeated in function tree_leaves to create dimension."""
    details_turtle.penup()
    details_turtle.goto(x, y)
    details_turtle.pendown()
    details_turtle.pencolor("black")
    details_turtle.setheading(0.0)
    
    i: int = 0
    while i < 2:
        details_turtle.right(120)
        details_turtle.forward(10)
        i += 1


def tree_leaves(leaves_turtle: Turtle, x: float, y: float) -> None:
    """Repeats function tree_details to create leave dimensions in the tree."""
    i: int = 0
    while i < 10:
        tree_details(leaves_turtle, x, y)
        tree_details(leaves_turtle, x + 20, y + 15)
        tree_details(leaves_turtle, x - 10, y - 40)
        tree_details(leaves_turtle, x + 40, y - 60)
        i += 1


def apple_body(apple_turtle: Turtle, x: float, y: float) -> None:
    """Draws the body of the apple that has fallen from the one of the trees."""
    apple_turtle.penup()
    apple_turtle.goto(x, y)
    apple_turtle.pendown()
    apple_turtle.pencolor("dark red")
    apple_turtle.fillcolor("dark red")
    apple_turtle.begin_fill()
    apple_turtle.circle(10)
    apple_turtle.end_fill()


if __name__ == "__main__":
    main()
