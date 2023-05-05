import random

# hash a formula
def h1(x, p, q):
    n = p * q
    print(n)
    return (x**2) % n

# list of prime numbers
primes = [3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101, 103, 107, 109, 113, 127, 131, 137, 139, 149, 151, 157, 163, 167, 173, 179, 181, 191, 193, 197, 199, 211, 223, 227, 229, 233, 239, 241, 251, 257, 263, 269, 271, 277, 281, 283, 293, 307, 311, 313, 317, 331, 337, 347, 349, 353, 359, 367, 373, 379, 383, 389, 397, 401, 409, 419, 421, 431, 433, 439, 443, 449, 457, 461, 463, 467, 479, 487, 491, 499, 503, 509, 521, 523, 541]

# choose randome primes
p = random.choice(primes)
q = random.choice(primes)

print(f"Primes Selected: P = {p}, Q = {q}")

# X value
x = 353

# Hashing with our function
hashed_value = h1(x, p, q)

print(f"Original X = {x}, Hashed value = {hashed_value}")

'''
One Way Property: This does satisfy the one way property even if we know n. We because of the Modulus, we don't know how many times the original function has 'wrapped around' so to speak. We can't predict the output.

Weak Collision Resistance: 

Strong Collision Resistance: 
'''