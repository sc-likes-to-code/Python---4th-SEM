# Define a simple custom exception
class MyCustomError(Exception):
    pass

# Function that raises the custom exception
def raise_custom_error():
    try:
        raise MyCustomError("Something went wrong!")
    except MyCustomError as e:
        print("Caught custom exception:", e)

# Calling the function
raise_custom_error()
