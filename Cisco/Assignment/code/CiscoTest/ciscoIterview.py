# To sort the list ----------------------------------------
def sortList_1():
        
    ls1 = [[31, 60], [10, 25], [30, 20], [20, 10], [45, 30]]


    for x in range(len(ls1)):

        print("ls1 = ", ls1)
        for index, val in enumerate(ls1):

        
            if index < len(ls1) - 1:
                if ls1[index][1] > ls1[index+1][1]:

                    temp = ls1[index]
                    ls1[index] = ls1[index+1]
                    ls1[index+1] = temp

                print("ls1 11111= ", ls1)


# To sort the list ----------------------------------------
def sortList_2():

    ls1 = [[31, 60], [10, 25], [30, 20], [20, 10], [45, 30]]

    for x in range(len(ls1)):
    
        nMin = ls1[x][1]
        for y in range(x, len(ls1)-1):

            if nMin > ls1[y][1]:

                temp = ls1[x]
                ls1[x] = ls1[y]
                ls1[y] = temp

    print("ls1 = ", ls1)
    

# ----------------------------------------------------------
# Decorator
#--------------
from inspect import getargspec

def Prod(a, b):

    print("division = ",a/b)

#@ Prod
def Dev(func):

    def subFunction(a, b):

        if a < b:
            a, b = b, a

        return func(a, b)


    return subFunction


def listComposition():

    lsNew = [i+y for i in ['a', 'b', 'c'] for y in ['x', 'y', 'z']]
    print("lsNew = ", lsNew)



#----------------------------------------------------------------------
# Function Calls
#------------------
#sortList_1()
#sortList_2()

# Decorator -----
#---------------------------------
# Function Calls
#-----------------

'''
#Prod(2, 4)
Dev1 = Dev(Prod)
print ("Arguments = ", len(getargspec(Dev1).args))
print("Dev1 = ", Dev1)
Dev1(2, 4)
'''

#listComposition()
