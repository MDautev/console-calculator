def add(a, b):
    return a + b

def substract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b==0:
        return "Error: Division by zero!"
    return a / b

def main():
    print("=== Console Calculator ===")
    print("Available operations: +, -, *, /")

    while True:
        try:
            num1 = float(input("Enter the first number: "))
            operator = input("Operator(+ - * /): ")
            num2 = float(input("Enter the second number: "))
        except ValueError:
            print("Please enter valid numbers.")
            continue

        if operator == "+":
            result = add(num1, num2)
        elif operator == "-":
            result = substract(num1, num2)
        elif operator == "*":
            result = multiply(num1, num2)
        elif operator == "/":
            result = divide(num1, num2)
        else:
            result = "Invalid operator"

        print("result:", result)

        again = input("Do you want to calculate again?(yes/no): ")
        if again.lower() != "yes":
            print("Goodbye! :)")
            break

if __name__ == "__main__":
    main()


