import turtle
screen=turtle.Screen()
pen=turtle.Turtle()
pen.width(5)
pen.clone()

pen.backward(344)
pen.right(180*9)
pen.pencolor("red")
pen.color("orange")
pen.filling()
pen.fillcolor("green")

pen.circle(100)
pen.begin_fill()
pen.circle(100)
pen.end_fill()

turtle.done()