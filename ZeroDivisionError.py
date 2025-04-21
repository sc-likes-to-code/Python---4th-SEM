def demonstrate_zero_division():
    try:
        # Trying to divide a number by zero
        result = 10 / 0
        print("Result:", result)
    except ZeroDivisionError as e:
        print("ZeroDivisionError occurred:", e)

# Calling the function
demonstrate_zero_division()
