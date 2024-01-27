def add(a, b):
    return a + b

def sub(a, b):
    return a - b

def mul(a, b):
    return a * b

def div(a, b):
    return a / b

a = int(input("Enter the first number: "))
b = int(input("Enter the second number: "))

print("The sum of the numbers is: ", add(a, b))
print("The difference of the numbers is: ", sub(a, b))
print("The product of the numbers is: ", mul(a, b))
print("The quotient of the numbers is: ", div(a, b))