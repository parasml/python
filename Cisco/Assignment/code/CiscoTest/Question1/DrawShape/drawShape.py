import turtle
import math

# define the function 
# for triangle 
def form_tri(side): 
    for i in range(3): 
        my_pen.fd(side) 
        my_pen.left(120) 
        side -= 10
  
def drawSquare():
    for x in range(0,4):
        my_pen.forward(100)
        my_pen.left(90)
        #my_pen.forward(100)
            
def drawRectangle():
    for x in range(0,4):
        if x%2 == 0:
            my_pen.forward(100)
        else:
            my_pen.forward(50)
        my_pen.left(90)
        #my_pen.forward(100)

def drawHexagoan(nside):
    
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

def drawTriangle(nSide):
    
    for n in range(3):

        my_pen.fd(nSide) 
        my_pen.left(120)




        



# Forming the window screen -------
tut = turtle.Screen() 
tut.bgcolor("green") 
tut.title("Turtle") 
  
my_pen = turtle.Turtle() 
my_pen.color("orange") 

#drawSquare()
#drawRectangle()
#drawHexagoan(100)
#drawCircle(40)
#drawRohmbus(30)
#drawTriangle(300)

#form_tri(300) 


#my_pen.setpos(100,100)
#print("Position = ", my_pen.pos())
#drawTriangle(300)

def drawFigure():
  
    nSide = 150

    drawHexagoan(nSide)
    getCursorCirclePos(nSide)
    drawCircle(nSide/2-10)
    getCursorRhombusPos(nSide/2-20)
    drawRohmbus(nSide/2-20)
    

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
    

drawFigure()

tut.mainloop()  # To avoid screen disapper at the end ------
        

''' 
# for different shapes 
side = 300
for i in range(10): 
    form_tri(side) 
    side -= 30
'''



