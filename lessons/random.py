"""Turtle."""


from turtle import Turtle, colormode, done
colormode(255)

def sunset(sunset_turtle: Turtle, x: float, y: float) -> None:
    """Creates a gradient sunset background in the landscape using rectangles."""
    i: int = 0
    while i < 8:
        sunset_turtle.penup()
        sunset_turtle.goto(x, (y - 50 * i))
        sunset_turtle.pendown()
        sunset_turtle.color(238 - 20 * i, (168 - i), 197 - i)
        sunset_turtle.pencolor(238 - 20 * i, (168 - i), 197 - i)
        sunset_turtle.fillcolor(238 - 20 * i, (168 - i), 197 - i)
        sunset_turtle.begin_fill()

        sunset_turtle.forward(748)
        sunset_turtle.right(90)
        sunset_turtle.forward(300)
        sunset_turtle.right(90)
        sunset_turtle.forward(748)
        sunset_turtle.right(90)
        sunset_turtle.forward(300)
        sunset_turtle.right(90)
        sunset_turtle.end_fill()
        i += 1
    done()


if __name__ == "__main__":
    main()