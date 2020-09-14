import turtle

wn = turtle.Screen()
wn.title("Chezz by Kevin")
wn.bgcolor("brown")
wn.setup(width=500, height=500)
wn.tracer(0)

#board
def draw_board():
    pen = turtle.Turtle()
    pen.penup()
    #pen.speed(3) #debugging
    pen.goto(-235, 240)
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
#squares
def draw_square(x, y):
    pen = turtle.Turtle()
    pen.pensize(width=60)
    pen.penup()
    pen.goto(x, y)
    pen.pendown()
    pen.shape("square")
    pen.color("white")
    #pen.forward()
#pieces
def draw_pawn(x, y):
    pawn = turtle.Turtle()
    pawn.penup()
    pawn.goto(x, y)
    #pawn.speed(0)
    pawn.shape("square")
    pawn.color("white")
    #pawn.shapesize(stretch_wid=2, stretch_len=2)
#main draw function
def draw():
    #drawing the board
    draw_board()
    #drawing the squares
    draw_square(-225, 229)
    #drawing the pawns
    draw_pawn(-150, -130)
    draw_pawn(-100, -130)
    draw_pawn(-50, -130)
    draw_pawn(0, -130)
    draw_pawn(50, -130)
    draw_pawn(100, -130)
    draw_pawn(150, -130)
    draw_pawn(200, -130)
    #drawing the rooks
    #drawing the knights
    #drawing the bishops
    #drawing the king
    #drawing the queen
#calling the main function
draw()
#main game loop
while True:
    wn.update()