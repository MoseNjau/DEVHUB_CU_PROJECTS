class Calculator:
    def __init__(self):
        pass

    def add(self, num1, num2):
        return num1 + num2

    def subtract(self, num1, num2):
        return num1 - num2

    def multiply(self, num1, num2):
        return num1 * num2

    def divide(self, num1, num2):
        if num2 != 0:
            return num1 / num2
        else:
            return "Error: Division by zero"

    def square(self, num):
        return num ** 2

    def square_root(self, num):
        if num >= 0:
            return num ** 0.5
        else:
            return "Error: Cannot compute the square root of a negative number"

    def exponentiate(self, base, exponent):
        return base ** exponent

    def factorial(self, num):
        if num < 0:
            return "Error: Factorial is not defined for negative numbers"
        elif num == 0 or num == 1:
            return 1
        else:
            result = 1
            for i in range(2, num + 1):
                result *= i
            return result


def main():
    calculator = Calculator()

    while True:
        print("Available Operations:")
        print("1: Addition")
        print("2: Subtraction")
        print("3: Multiplication")
        print("4: Division")
        print("5: Square")
        print("6: Square Root")
        print("7: Exponentiation")
        print("8: Factorial")
        print("0: Exit")

        choice = input("Enter the operation number (0 to exit): ")

        if choice == '0':
            print("Exiting the calculator. Goodbye!")
            break

        if choice.isdigit() and 1 <= int(choice) <= 8:
            num1 = float(input("Enter the first number: "))
            if int(choice) in [5, 6, 8]:
                result = getattr(calculator, calculator.operations[int(choice)].lower())(num1)
            else:
                num2 = float(input("Enter the second number: "))
                result = getattr(calculator, calculator.operations[int(choice)].lower())(num1, num2)

            print(f"Result: {result}")
        else:
            print("Invalid operation choice. Please enter a valid operation number.")


if __name__ == "__main__":
    main()
