# Define a custom exception for formula errors
class FormulaError(Exception):
    pass

def interactive_calculator():
    while True:
        user_input = input(">>> ")
        
        if user_input.lower() == "quit":
            break
        
        parts = user_input.split()
        
        if len(parts) != 3:
            print("FormulaError: Input must have two numbers and an operator.")
            continue
        
        num1_str, operator, num2_str = parts
        
        try:
            num1 = float(num1_str)
            num2 = float(num2_str)
        except ValueError:
            print("FormulaError: Both operands must be numbers.")
            continue
        
        if operator not in ['+', '-']:
            print("FormulaError: Operator must be '+' or '-'.")
            continue
        
        if operator == '+':
            print(num1 + num2)
        elif operator == '-':
            print(num1 - num2)

# Run the calculator
interactive_calculator()
