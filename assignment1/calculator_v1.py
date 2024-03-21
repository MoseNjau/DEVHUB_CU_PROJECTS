# The getattr method is used to dynamically access a method based on a constructed string, which is the lowercase version of the operation name. In Python, method names are case-sensitive, so the dynamically constructed string must match the actual method name in the class.

class Calculator:
    def __init__(self) -> None:
        self.operations = {
            1: 'Addition',
            2: 'Subtraction',
            3: 'Multiplication',
            4: 'Division',
            5: 'Square',
            6: 'Square Root',
            7: 'Exponentiation',
            8: 'Factorial'
        }

    def display_operations(self):
        print("Available Operations")
        for key, value in self.operations.items():
            print(f"{key}: {value}")
    
    def add(self, num1, num2):
        return num1 + num2
    
    def subtract(self, num1, num2):
        return num1 - num2

    def multiply(self, num1, num2):
        return num1 * num2
    
    def division(self, num1, num2):
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
            print(f"Cannot compute the squareroot of negative number {num}")

    def exponentiation(self, base, exponent):
        return base ** exponent
    
    def factorial(self, num):
        if num < 0:
            return "Error: Factorial is not defined for negative numbers"
        elif num == 0 or num == 1:
            return 1
        else:
            result = 1
            for i in range(2, int(num) + 1):  # Convert num to an integer
                result *= i
            return result

        
calculator = Calculator()
calculator.display_operations()

operation_choice = int(input("Enter the operation number: "))

if operation_choice in calculator.operations:
    if operation_choice in [5, 6, 8]:
        num = float(input("Enter a number: "))
        result = getattr(calculator, calculator.operations[operation_choice].lower())(num)
    else:
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))
        result = getattr(calculator, calculator.operations[operation_choice].lower())(num1, num2)

    print(f"Result of {calculator.operations[operation_choice]}: {result}")
else:
    print("Invalid operation choice.")
