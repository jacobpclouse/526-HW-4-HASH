import math

def h1(x, n):
    return pow(x, 2) % n

def find_collision(n, max_tries=1000):
    for i in range(max_tries):
        x = math.floor(math.sqrt(n)) + i
        hx = h1(x, n)
        for y in range(x+1, n):
            hy = h1(y, n)
            if hx == hy:
                return x, y
    return None

n = 1346398753
x, y = find_collision(n)
if x is not None:
    print(f"Collision found: h({x}) = h({y})")
else:
    print("No collision found")
