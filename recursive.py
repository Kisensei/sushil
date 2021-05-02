import turtle
screem=turtle.Turtle()
pen=turtle.Turtle()
def drawcircle(x,y,z):
    pen.penup()
    pen.speed(0)
    pen.goto(x,y-z)
    pen.pendown()
    pen.circle(z)


def make_picture(x,y,z):
    if z<10:
      drawcircle(x,y,z)
    else:
        drawcircle(x, y, z)
        make_picture(x,y,z/2)
        make_picture(x+4,y+4,z+4)
        make_picture(x - 4, y4)

make_picture(0,0,0)
turtle.done()
