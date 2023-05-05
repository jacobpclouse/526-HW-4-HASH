def custom_hash(input_str):
    # Initialize hash value to 0
    hash_val = 0
    # Iterate over each character in the string
    for char in input_str:
        # Convert the character to its ASCII code
        ascii_code = ord(char)
        # Update the hash value with the ASCII code
        hash_val = (hash_val * 31) + ascii_code
    # Return the hash value
    return hash_val
