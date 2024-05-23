try:
    num1 = float(input("Enter first number: "))
    operation = input("Enter operation: ")
    num2 = float(input("Enter second number: "))

    def calculator(operation,num1,num2):
        if operation == '+':
            return num1 + num2
        elif operation == '-':
            return num1 - num2
        elif operation == '*':
            return num1 * num2
        elif operation == '/':
            if num2 == 0:
                raise ValueError("Division by zero is not possible")
            return num1 / num2
        else:
            raise ValueError("Unsupported operation")

    print(calculator(operation, num1, num2))
except ValueError as e:
    print("Error:", e)


    