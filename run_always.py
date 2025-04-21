def run_always():
    try:
        # Code that may or may not raise an error
        value = 10 / 2
        print("Try block executed. Value:", value)
    except ZeroDivisionError as e:
        print("Exception occurred:", e)
    finally:
        # This block always runs
        print("This block runs no matter what")

# Calling the function
run_always()
