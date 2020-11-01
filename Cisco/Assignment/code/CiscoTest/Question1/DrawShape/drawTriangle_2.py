import turtle
import math

# define the function 
# for triangle

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


def drawFigure():

    smallTriangleSide = 30
    nsmallDist = 10
    nBigDist = 100
  

    # 1st Triangle ---------

    drawTriangle(smallTriangleSide)

    my_pen.forward(smallTriangleSide)
    my_pen.left(120)

    my_pen.forward(nsmallDist)

    my_pen.right(120)

    my_pen.forward(nBigDist)

    #2nd Triangle----------

    
    my_pen.left(-120)
    my_pen.forward(nsmallDist)
    my_pen.left(120)


    drawTriangle(smallTriangleSide)

    my_pen.left(60)

    my_pen.forward(smallTriangleSide-nsmallDist)

    my_pen.left(60)

    my_pen.forward(nBigDist)

    # 3rd Traingle----------

    my_pen.left(-120)

    my_pen.forward(nsmallDist)

    my_pen.left(120)

    drawTriangle(smallTriangleSide)


    my_pen.left(60)

    my_pen.forward(smallTriangleSide-nsmallDist)

    my_pen.left(60)

    my_pen.forward(nBigDist)

    
# -----------------------------------------------------------
# Function Calls
#------------------
drawFigure()

tut.mainloop()  # To avoid screen disapper at the end ------




