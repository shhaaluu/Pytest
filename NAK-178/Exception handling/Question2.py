print("Program to handle multiple errors with one except statement")

def fun(a):
    if a < 4:
        b = a/(a-3)
    print("Value of b = ", b)

try:
    fun(3)
    fun(5)

except ZeroDivisionError:
    print("ZeroDivisionError occurred and handled")

    
