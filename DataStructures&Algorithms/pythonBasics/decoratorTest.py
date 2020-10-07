#-----------------------------------
# To test Decorator
#------------------------

def ExistingFunc(func1):

    def nowExecution(*args, **kwargs):

        print("1111111111111111111")
        func1(*args, **kwargs)
        print("22222222222222222222")

    return nowExecution

#---------------------------------------
# New Function
#--------------

@ExistingFunc
def NewFunc(panel):
    print("This is a new function")

    if panel == 'admin':
        print("Its an Admin Account")
    else:
        print("Its an USER Account")


# Function Calls ------
NewFunc("NonAdmin")

'''
# '@ExistingFunc' Replaces the below code --------------------------
funcDec = ExistingFunc(NewFunc)
print("funcDec = ", funcDec)
funcDec()
'''

