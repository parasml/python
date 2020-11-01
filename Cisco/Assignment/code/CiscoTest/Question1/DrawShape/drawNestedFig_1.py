import turtle
import math


def drawHexagoan(nside):
    
    #print("Initial Pos = ", my_pen.pos())
    for x in range(0,6):
        my_pen.forward(nside)
        my_pen.left(60)


def drawCircle(nRadius):
    my_pen.circle(nRadius)

def drawRohmbus(nSide):
    
    my_pen.left(45)
    for x in range(4):
        my_pen.forward(nSide)
        my_pen.left(90)

def getCursorRhombusPos(nSide):
    
    my_pen.penup()
    PosX = my_pen.pos()[0]
    PosY = my_pen.pos()[1]
    #PosY = 100
    PosY += nSide/2  # Radius
    #print("PosY = ", PosY)
    my_pen.goto(PosX,PosY)
    my_pen.pendown()
    

def getCursorCirclePos(nSide):
    
    print("Sin = ", math.sin(math.radians(60)))
    my_pen.penup()
    PosX = nSide/2
    PosY = nSide*math.sin(math.radians(60))
    PosY -= nSide/2-10  # Radius
    my_pen.goto(PosX,PosY)
    my_pen.pendown()

def drawFigure():
      
    nSide = 150

     #To draw outer hexagoan------------
    drawHexagoan(nSide)
    # Move cursor to draw Circle-------
    getCursorCirclePos(nSide)
    # To draw circle ----------------
    drawCircle(nSide/2-10)
    # Move cursor to draw Circle-------
    getCursorRhombusPos(nSide/2-20)
    # To draw rohmbus ----------
    drawRohmbus(nSide/2-20)

# =============================================================================
# Forming the window screen -------
tut = turtle.Screen() 
tut.bgcolor("green") 
tut.title("Turtle") 
  
my_pen = turtle.Turtle() 
my_pen.color("orange") 


drawFigure()

tut.mainloop()  # To avoid screen disapper at the end ------
        



