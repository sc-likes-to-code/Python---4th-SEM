def digit_difference(number):
    # Convert the number to a string to access digits
    num_str = str(number)
    
    # Create the largest and smallest numbers by sorting the digits
    largest = int(''.join(sorted(num_str, reverse=True)))
    smallest = int(''.join(sorted(num_str)))
    
    # Return the difference
    return largest - smallest

# Example usage
number = 213
result = digit_difference(number)
print(result)  # Output: 198
