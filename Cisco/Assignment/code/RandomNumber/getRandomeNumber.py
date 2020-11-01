#----------------------------------------------
# To generate randome number
#------------------------------
import random

from numpy.random import seed
from numpy.random import rand

def getRandomeNumber():
    
    # Random int value -------
    value = random.randint(10000, 100000)

    print("value = ", value)

    # Floating point random values------
    # Generates a random number between (0, 1)
    print(random.random())

    # Random Gaussian value -------
    # From point 0 to deviation of 1
    value = random.gauss(0, 1)
    print("value = ", value)


    # Get random number from from numpy class ---------------
    numpyValue = rand()
    print("numpyValue = ", numpyValue)



#----------------------------------------------
# Function Calls
#------------------
getRandomeNumber()