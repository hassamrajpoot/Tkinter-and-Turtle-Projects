import turtle
from math import cos as cosine, pi as pi


def triangle(turtle_name, sides_length):
    global x_position
    global y_position
    turtle_name = turtle.Turtle()
    turtle_name.penup()
    turtle_name.goto((x_position, y_position))
    turtle_name.pendown()
    turtle_name.speed(0)
    turtle_name.color('#BADE1F')
    turtle_name.pensize(10)
    turtle_name.setheading(90)
    turtle_name.forward(sides_length)
    turtle_name.left(120)
    turtle_name.forward(sides_length)
    turtle_name.left(120)
    turtle_name.forward(sides_length)
    turtle_name.penup()
    turtle_name.goto((x_position, y_position))
    turtle_name.pendown()
    turtle_name.setheading(0)


def square(turtle_name, sides_length):
    turtle_name = turtle.Turtle()
    turtle_name.penup()
    turtle_name.goto((x_position, y_position))
    turtle_name.pendown()
    turtle_name.speed(0)
    turtle_name.pensize(10)
    turtle_name.color('black')
    for i in range(4):
        turtle_name.forward(sides_length)
        turtle_name.left(90)
    turtle_name.penup()
    turtle_name.goto((x_position, y_position))
    turtle_name.pendown()
    turtle_name.setheading(0)


def hexagon(turtle_name, sides_length):
    turtle_name = turtle.Turtle()
    turtle_name.penup()
    turtle_name.color('red')
    new_x = x_position + length
    turtle_name.goto((new_x, y_position))
    turtle_name.pendown()
    turtle_name.speed(0)
    turtle_name.pensize(10)
    turtle_name.setheading(90)
    turtle_name.forward(sides_length)
    turtle_name.right(120)
    turtle_name.forward(sides_length)
    to_use_in_future = turtle_name.pos()
    turtle_name.right(120)
    turtle_name.forward(sides_length)
    turtle_name.penup()
    turtle_name.goto(to_use_in_future)
    turtle_name.pendown()
    turtle_name.setheading(0)
    turtle_name.left(30)
    turtle_name.forward(sides_length)
    turtle_name.right(120)
    turtle_name.forward(sides_length)
    turtle_name.right(120)
    turtle_name.forward(sides_length)
    turtle_name.penup()
    turtle_name.goto((new_x, y_position))
    turtle_name.pendown()
    turtle_name.setheading(90)
    turtle_name.color('#1FDE85')
    for i in range(6):
        turtle_name.forward(sides_length)
        turtle_name.right(60)
    turtle_name.penup()
    turtle_name.goto((x_position, y_position))
    turtle_name.pendown()
    turtle_name.setheading(0)


def pentagon(turtle_name, sides_length):
    turtle_name = turtle.Turtle()
    turtle_name.penup()
    turtle_name.goto((x_position+length, y_position))
    turtle_name.color('#AB1FDE')
    turtle_name.pendown()
    turtle_name.speed(0)
    turtle_name.pensize(10)
    turtle_name.setheading(90)
    for i in range(5):
        turtle_name.forward(sides_length)
        turtle_name.right(72)
    turtle_name.penup()
    turtle_name.goto((x_position, y_position))
    turtle_name.pendown()
    turtle_name.setheading(0)


def snake(turtle_name, sides_length):
    triangle(turtle_name, sides_length)
    square(turtle_name, sides_length)
    global length
    length = sides_length
    hexagon(turtle_name, sides_length)
    a = sides_length
    b = sides_length
    c = ((a ** 2) + (b ** 2) - (2 * a * b) * cosine(120 * (pi / 180))) ** 0.5
    length = c + sides_length
    hexagon(turtle_name, sides_length)
    length = length + c
    pentagon(turtle_name, sides_length)


#==========================================================
def main():
    """
    This program draws a snake using different shapes
    """
    global x_position
    global y_position
    global length
    y_position = 0
    x_position = -250
    length = 0
    snake('rabbit', 100)


if __name__ == '__main__':
    main()

turtle.done()  # used this because turtle.getscreen().exitonclick()  gives :- Unresolved attribute reference 'exitonclick' for class 'TurtleScreen'
