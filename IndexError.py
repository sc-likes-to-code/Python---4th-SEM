def demonstrate_index_error():
    try:
        # Defining a list with 3 elements
        numbers = [1, 2, 3]
        # Trying to access an index that doesn't exist
        print(numbers[5])
    except IndexError as e:
        print("IndexError occurred:", e)

# Calling the function
demonstrate_index_error()
