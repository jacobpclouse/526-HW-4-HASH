# =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
# Importing Libraries / Modules 
# =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
import math


# =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
# Functions
# =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-

# --- Function to execute Hash A ---
def h1(x, n):
    return pow(x, 2) % n

# --- Function to find collisions for Hash A (find a pair (x, y) such that h2(x) = h2(y))---
def find_collision(n, max_tries=1000):
    for i in range(max_tries):
        x = math.floor(math.sqrt(n)) + i
        hx = h1(x, n)
        for y in range(x+1, n):
            hy = h1(y, n)
            if hx == hy:
                return x, y
    return None


# =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
# MAIN 
# =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-

# execute function with same n
n = 1346398753
x, y = find_collision(n)

# print out when finds collision
if x is not None:
    print(f"Collision found: h({x}) = h({y})")
else:
    print("No collision found")
