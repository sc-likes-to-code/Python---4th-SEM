def raise_custom_exception(age):
    try:
        if age < 0:
            raise ValueError("Age cannot be negative!")
        print("Valid age entered:", age)
    except ValueError as e:
        print("Exception raised:", e)

# Calling the function with invalid input to trigger the exception
raise_custom_exception(-5)
