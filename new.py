print("introduction to python assignment")
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
operation= input("enter operation (+-/*):")
if operation == '+':
    result = num1 + num2
elif operation == '-':
    result = num1 - num2
elif operation == '/':
    result = num1 / num2
elif operation == '*':
    result = num1 * num2

print(f"The result of {num1} {operation} {num2} is {result}") 
