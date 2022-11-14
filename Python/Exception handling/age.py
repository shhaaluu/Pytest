a = 10
b = 2

try:
    print("resource open")
    c = a/b
    print(c)
    k = int(input("Enter a number "))
    print(k)


except ZeroDivisionError as e:
    print("Hey, You cannot divide a number by zero", e)

except ValueError as e:
    print("Invalid Input")

finally:
    print("resourse closed")
