'''
x = 6
y = 6.0

print("x = ", id(x))
print("x = ", id(y))

x+=1

print("11111x = ", id(x))
print("x = ", id(y))


print("x = ", x)
print("y = ", y)

x+=2

print("222222x = ", id(x))
print("x = ", id(y))


class Test:

    def __init__(self):
        pass

    def connectServer(self):
        print("Inside connect Server --------")



def connectLocal():
    print("Local Connection --------")


#-----------------------------------
# Function Calls
#------------------
oTest = Test()

oTest.connectServer()

oTest.connectServer = connectLocal

oTest.connectServer()
'''

s = 'prashan'

print(s[::-1])



