import hashlib
import random

def h2(message):
    """
    Hash function h2 that takes a message as input
    and returns a 160-bit hash value
    """
    hash_value = message[0]
    for block in message[1:]:
        hash_value ^= block
    return hash_value

def find_collision():
    """
    Function to find a pair (x, y) such that h2(x) = h2(y)
    """
    # Initialize a dictionary to store the hash values
    hash_dict = {}

    # Generate a random message x
    x = [random.getrandbits(160) for i in range(10)]
    x_hash = h2(x)

    # Check if x_hash is already in the dictionary
    if x_hash in hash_dict:
        return (x, hash_dict[x_hash])

    # Add x_hash to the dictionary
    hash_dict[x_hash] = x

    # Generate a new random message y and check for collision
    while True:
        y = [random.getrandbits(160) for i in range(10)]
        y_hash = h2(y)

        if y_hash in hash_dict:
            return (y, hash_dict[y_hash])
        else:
            hash_dict[y_hash] = y

# Find a collision and print the result
x, y = find_collision()
print("Collision found!")
print("x: ", x)
print("y: ", y)
print("h2(x): ", h2(x))
print("h2(y): ", h2(y))
