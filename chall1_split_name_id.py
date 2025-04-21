def parse_encoded_string(encoded_str):
    # Split the string by '0' and filter out any empty strings
    parts = list(filter(None, encoded_str.split('0')))
    
    # Return the parsed data as a dictionary
    return {
        "first_name": parts[0],
        "last_name": parts[1],
        "id": parts[2]
    }

# Example usage
encoded_str = "Robert000Smith000123"
result = parse_encoded_string(encoded_str)
print(result)
