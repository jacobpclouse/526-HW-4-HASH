# =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
# Importing Libraries / Modules 
# =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
# import hashlib
import random

# =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
# Functions
# =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-

# --- Function to execute Hash b ---
def h2(message):
    hash_value = message[0]
    for block in message[1:]:
        hash_value ^= block
    # 160 bit output 
    return hash_value


# --- Function to find collisions for Hash B (find a pair (x, y) such that h2(x) = h2(y))---
def find_collision():
    hash_dict = {}
    x = [random.getrandbits(160) for i in range(10)]
    x_hash = h2(x)
    if x_hash in hash_dict:
        return (x, hash_dict[x_hash])
    hash_dict[x_hash] = x
    while True:
        y = [random.getrandbits(160) for i in range(10)]
        y_hash = h2(y)

        if y_hash in hash_dict:
            return (y, hash_dict[y_hash])
        else:
            hash_dict[y_hash] = y


# =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
# MAIN 
# =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-

# Find a collision and print the result
x, y = find_collision()
print("Collision found!")
print("x: ", x)
print("y: ", y)
print("h2(x): ", h2(x))
print("h2(y): ", h2(y))


# NOTE: This is not an incredibly efficient method of finding conflicts but it gets the job done