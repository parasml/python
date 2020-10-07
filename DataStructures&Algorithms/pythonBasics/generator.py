#-------------------------------------------------------------------
# Generator
#------------

def fiboOld():
    yield 10
    yield 100
    yield 1000


def fibo():

    a = 0
    b=1

    while True:
        yield a
        a, b = b, a+b

#---------------------------
'''
for f in fibo():
    print("f = ", f)
'''

for f in fibo():
    print("f = ", f)
    if f > 50:
        break