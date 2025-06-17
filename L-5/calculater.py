# simple calculater using ladder statements


# perform for calculation

dec = True
while True:

    operator = input("Enter an operator(+ , - , * , /):")

    if operator == '+':
        num1 = float(input("Enter first Number : "))
        num2 = float(input("Enter second Number : "))
        result = num1 + num2
        print(f"sum of {num1} + {num2} = {result}")

    elif operator == '*':
        num1 = float(input("Enter first Number : "))
        num2 = float(input("Enter second Number : "))
        result = num1 * num2
        print(f"sum of {num1} * {num2} = {result}")

    elif operator == '/':
        num1 = float(input("Enter first Number : "))
        num2 = float(input("Enter second Number : "))
        result = num1 / num2
        print(f"sum of {num1} / {num2} = {result}")

    elif operator == '-':
        num1 = float(input("Enter first Number : "))
        num2 = float(input("Enter second Number : "))
        result = num1 - num2
        print(f"sum of {num1} - {num2} = {result}")

    else:
        dec = False
        print(f"This Operator not found")
