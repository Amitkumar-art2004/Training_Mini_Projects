import math
operator = input("Enter operator (+, -, *, /, ^, %, log, x!, sin, cos, tan): ")
if operator in ["+", "-", "*", "/", "^", "%"]:
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))

    if operator == "+":
        print("Result:", num1 + num2)

    elif operator == "-":
        print("Result:", num1 - num2)

    elif operator == "*":
        print("Result:", num1 * num2)

    elif operator == "/":
        if num2 == 0:
            print("Cannot divide by zero!")
        else:
            print("Result:", num1 / num2)

    elif operator == "^":
        print("Result:", num1 ** num2)

    elif operator == "%":
        print("Remainder:", num1 % num2)

elif operator == "x!":
    x = int(input("Enter a number: "))
    fact = 1
    for i in range(1, x + 1):
        fact *= i
    print("Factorial:", fact)

elif operator in ["sin", "cos", "tan"]:
    x = float(input("Enter angle in degrees: "))
    if operator == "sin":
        print("Result:", math.sin(math.radians(x)))

    elif operator == "cos":
        print("Result:", math.cos(math.radians(x)))

    else:
        print("Result:", math.tan(math.radians(x)))

elif operator == "log":
    x = float(input("Enter a number: "))
    print("Result:", math.log10(x))

else:
    print("Invalid operator!")    
