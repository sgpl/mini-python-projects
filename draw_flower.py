import turtle


def movement(turtle_name, color, heading_direction):
    """Defines the movement to be used in draw_flower."""
    turtle_name.color(color)
    turtle_name.home()
    turtle_name.setheading(heading_direction)
    turtle_name.backward(149)


def draw_flower():
    """Draws a multicolored flower."""
    window = turtle.Screen()
    window.bgcolor("red")

    sharad = turtle.Turtle()
    sharad.color("yellow")
    sharad.shape("turtle")
    sharad.speed(13)

    count_1 = 50
    while count_1 != 0:
        x = 4
        while x > 0:
            sharad.forward(150)
            sharad.right(70)
            if count_1 == 10:
                movement(sharad, "blue", 0)
            if count_1 == 20:
                movement(sharad, "green", 72)
            if count_1 == 30:
                movement(sharad, "black", 144)
            if count_1 == 40:
                movement(sharad, "pink", 216)
            if count_1 == 50:
                movement(sharad, "brown", 288)
            sharad.stamp()
            x -= 1
        count_1 -= 1

    sharad.home()
    sharad.setheading(90)
    count_2 = 250
    while count_2 != 0:
        sharad.backward(15)
        sharad.stamp()
        count_2 -= 1
    window.exitonclick()


draw_flower()
