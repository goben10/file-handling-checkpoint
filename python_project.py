import math

class Calculator:
    def __init__(self):
        # Initialize dictionary with basic operations
        self.operations = {
            '+': lambda x, y: x + y,
            '-': lambda x, y: x - y,
            '*': lambda x, y: x * y,
            '/': lambda x, y: x / y if y != 0 else math.inf  # Prevent division by zero
        }

    def add_operation(self, symbol, func):
        """Add a new operation to the calculator"""
        self.operations[symbol] = func

    def calculate(self, num1, op, num2=None):
        """Perform calculation using stored operations"""
        try:
            # Validate numeric input
            if not isinstance(num1, (int, float)):
                raise ValueError("First input is not a number.")
            if num2 is not None and not isinstance(num2, (int, float)):
                raise ValueError("Second input is not a number.")

            # Check if operation exists
            if op not in self.operations:
                raise ValueError(f"Invalid operation '{op}'.")

            # Handle unary operations like sqrt and log
            if num2 is None:
                result = self.operations[op](num1)
            else:
                result = self.operations[op](num1, num2)

            return result

        except Exception as e:
            print(f"Error: {e}")
            raise

# --------------------------
# Define advanced operations
# --------------------------
def power(x, y):
    """Exponentiation"""
    return x ** y

def square_root(x):
    """Square root"""
    if x < 0:
        raise ValueError("Cannot compute square root of a negative number.")
    return math.sqrt(x)

def logarithm(x):
    """Natural logarithm"""
    if x <= 0:
        raise ValueError("Logarithm undefined for zero or negative values.")
    return math.log(x)

# --------------------------
# Main program
# --------------------------
if __name__ == "__main__":
    calc = Calculator()

    # Add advanced operations
    calc.add_operation('^', power)
    calc.add_operation('sqrt', square_root)
    calc.add_operation('log', logarithm)

    print("🔹 Welcome to the Python Calculator 🔹")
    print("Available operations: +, -, *, /, ^, sqrt, log")
    print("Type 'exit' anytime to quit.\n")

    while True:
        # Get user input
        user_input = input("Enter calculation (e.g., 5 + 2) or 'exit': ")

        if user_input.lower() == "exit":
            print("👋 Exiting calculator. Goodbye!")
            break

        # Handle unary and binary operations differently
        try:
            parts = user_input.split()

            if len(parts) == 2:  # Unary operations like sqrt 9
                op, num1 = parts
                num1 = float(num1)
                result = calc.calculate(num1, op)
                print(f"Result: {result}\n")

            elif len(parts) == 3:  # Binary operations like 5 + 2
                num1, op, num2 = parts
                num1, num2 = float(num1), float(num2)
                result = calc.calculate(num1, op, num2)
                print(f"Result: {result}\n")

            else:
                print("❌ Invalid input format. Try again.\n")

        except Exception as e:
            print(f"⚠️ Error: {e}\n")
