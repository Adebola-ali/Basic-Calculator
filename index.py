# Basic Calculator Program
firstValue = int(input('Enter first value: '))
secondValue = int(input('Enter second value: '))
operation = input('Enter operation (+, -, *, /): ') c
result = 0  
if operation == '+':
    result = firstValue + secondValue
elif operation == '-':
    result = firstValue - secondValue
elif operation == '*':
    result = firstValue * secondValue
elif operation == '/':
    if secondValue != 0:
        result = firstValue / secondValue
    else:
        print("Error: Division by zero is not allowed.")
else:
    print("Error: Invalid operation.")
if result != 0:
    print('The result of', firstValue, operation, secondValue, 'is:', result)

    

