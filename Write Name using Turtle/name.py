import turtle


def draw_V(turtle_name):
    global x_position
    global y_position
    turtle_name = turtle.Turtle()
    turtle_name.penup()
    turtle_name.goto((x_position, y_position))
    turtle_name.pendown()
    turtle_name.speed(0)
    turtle_name.pensize(10)
    turtle_name.color('lime')
    turtle_name.setheading(0)
    turtle_name.left(120)
    turtle_name.forward(100)
    turtle_name.penup()
    turtle_name.goto((x_position, y_position))
    turtle_name.pendown()
    turtle_name.setheading(0)
    turtle_name.left(60)
    turtle_name.forward(100)
    turtle_name.setheading(0)


def draw_A(turtle_name):
    global x_position
    global y_position
    turtle_name = turtle.Turtle()
    turtle_name.penup()
    turtle_name.goto((x_position, y_position))
    turtle_name.pendown()
    turtle_name.speed(0)
    turtle_name.color('turquoise')
    turtle_name.pensize(10)
    turtle_name.setheading(0)
    turtle_name.left(90)
    turtle_name.forward(40)
    position = turtle_name.pos()
    turtle_name.right(90)
    turtle_name.forward(50)
    turtle_name.goto(position)
    turtle_name.setheading(90)
    turtle_name.forward(50)
    turtle_name.right(90)
    turtle_name.forward(50)
    turtle_name.right(90)
    turtle_name.forward(90)
    turtle_name.setheading(0)


def draw_N(turtle_name):
    global x_position
    global y_position
    turtle_name = turtle.Turtle()
    turtle_name.penup()
    turtle_name.goto((x_position, y_position))
    turtle_name.pendown()
    turtle_name.speed(0)
    turtle_name.color('mediumorchid')
    turtle_name.pensize(10)
    turtle_name.setheading(90)
    turtle_name.forward(90)
    turtle_name.right(140)
    turtle_name.forward(120)
    turtle_name.setheading(90)
    turtle_name.forward(90)
    turtle_name.setheading(0)


#==========================================================
def main():
    global x_position
    global y_position
    x_position = -100
    y_position = 0
    '''
    Running this file writes my nick using turtle
    '''
    draw_V('bunny')
    x_position += 100
    draw_A('bunny')
    x_position += 100
    draw_N('bunny')


if __name__ == '__main__':
    main()

#turtle.getscreen().exitonclick()  # keeps the turtle graphics window open

turtle.done()  # used this because  , turtle.getscreen().exitonclick() gives :- Unresolved attribute reference 'exitonclick' for class 'TurtleScreen'
