def add(numbers):
    return sum(numbers)

def subtract(numbers):
    result = numbers[0]
    for num in numbers[1:]:
        result -= num
    return result

def multiply(numbers):
    result = 1
    for num in numbers:
        result *= num
    return result

def divide(numbers):
    result = numbers[0]
    for num in numbers[1:]:
        if num == 0:
            return "Error: Division by zero is not allowed."
        result /= num
    return result
def exponent(numbers):
    if len(numbers) != 2:
        return "Error: Exponentiation requires exactly two numbers."
    base, exp = numbers
    return base ** exp

def calculator():
    print("Simple Calculator for Multiple Numbers")
    print("Operations: ")
    print("1. Addition (+)")
    print("2. Subtraction (-)")
    print("3. Multiplication (*)")
    print("4. Division (/)")
    print("5. Exponents (^)")

    try:
        numbers = list(map(float, input("Enter numbers separated by space: ").split()))
        operation = input("Choose an operation : ")
        operations = {
            '+': add,
            '-': subtract,
            '*': multiply,
            '/': divide,
            '^': exponent
        }
        if operation in operations:
            result = operations[operation](numbers)
            print(f"The result is: {result}")
        else:
            print("Invalid operation. Please choose from +, -, *, or /.")

    except ValueError:
        print("Invalid input. Please enter numeric values.")

calculator()
