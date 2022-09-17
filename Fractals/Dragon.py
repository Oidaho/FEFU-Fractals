import turtle

def StartDragon():
    turtle.tracer(0, 0)
    turtle.setup(1920, 1080)

    turtle.penup()
    turtle.setpos(0, 200)
    turtle.width(1)
    turtle.pendown()

    rule = 'R'
    iterations = 17

    for iteration in range(iterations):
        reverse = rule[::-1]
        reverse = reverse.replace('R', '.')
        reverse = reverse.replace('L', 'R')
        reverse = reverse.replace('.', 'L')
        rule = rule + 'R' + reverse

    for direction in rule:
        if direction == 'R':
            turtle.right(90)
        if direction == 'L':
            turtle.left(90)
        turtle.forward(1)

    turtle.update()
    turtle.done()



