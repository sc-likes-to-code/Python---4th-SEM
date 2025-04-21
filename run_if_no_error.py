def run_if_no_error():
    try:
        # Code that may or may not raise an error
        result = 5 + 3
        print("Try block executed successfully. Result:", result)
    except Exception as e:
        print("An error occurred:", e)
    else:
        # This block runs only if no exception occurs in try
        print("No errors occurred! Running else block...")

# Calling the function
run_if_no_error()
