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
    nRadius = 10
  

    # 1st Triangle ---------

    my_pen.circle(nRadius)

    my_pen.left(-70)
    my_pen.forward(50)
    
    #------
    my_pen.circle(nRadius)

    my_pen.circle(nRadius, 90)

    my_pen.left(-30)
    my_pen.forward(50)

    #------

    my_pen.circle(-nRadius)
    my_pen.circle(nRadius, 20)
    my_pen.forward(50)

    #------
    my_pen.circle(nRadius)
    my_pen.circle(nRadius, 70)
    my_pen.forward(50)

    #--------
    my_pen.left(70)
    my_pen.circle(-nRadius)

    #--------
    my_pen.circle(-nRadius, 60)
    my_pen.left(90)
    my_pen.forward(140)
    #my_pen.circle(-nRadius)

    return

   
   
    
# -----------------------------------------------------------
# Function Calls
#------------------
drawFigure()

tut.mainloop()  # To avoid screen disapper at the end ------




