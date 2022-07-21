import turtle


def StartDragon():
    directions = 'R'
    iterations = 17
    line_length = 1
    angle = 90

    turtle.tracer(0, 0)
    turtle.setup(1920, 1080)

    turtle.penup()
    turtle.setpos(0, 200)
    turtle.width(1)
    turtle.pendown()

    for i in range(iterations):
        reverse = directions[::-1]
        reverse = reverse.replace('R', '-').replace('L', 'R').replace('-', 'L')
        directions = directions + 'R' + reverse

    for a in directions:
        if a == 'R':
            turtle.right(angle)
        if a == 'L':
            turtle.left(angle)
        turtle.forward(line_length)

    turtle.update()
    turtle.done()



