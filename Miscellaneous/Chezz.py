import turtle

wn = turtle.Screen()
wn.title("Chezz by Kevin")
wn.bgcolor("brown")
wn.setup(width=500, height=500)
#wn.tracer(0)

#board
def draw_board(x, y):
    pen = turtle.Turtle()
    pen.penup()
    #pen.speed(3) #debugging
    pen.goto(x, y)
    pen.pendown()
    pen.shape("turtle")
    pen.forward(450)
    pen.right(90)
    pen.forward(450)
    pen.right(90)
    pen.forward(450)
    pen.right(90)
    pen.forward(460)
    pen.penup()
    #removing the turtle
    pen.color("brown")
draw_board(-235, 240)
#pieces
def draw_pawn(x, y):
    pawn = turtle.Turtle()
    #pawn.speed(0)
    pawn.shape("square")
    pawn.color("white")
    #pawn.shapesize(stretch_wid=2, stretch_len=2)
    pawn.penup()
    pawn.goto(x, y)


#while True:
draw_pawn(50, -5)

#main game loop
while True:
    wn.update()