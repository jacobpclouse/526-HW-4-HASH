import random

# hash a formula
def h1(x, p, q):
    n = p * q
    print(f"N = {n}")
    return (x**2) % n

# list of prime numbers
primes = [3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101, 103, 107, 109, 113, 127, 131, 137, 139, 149, 151, 157, 163, 167, 173, 179, 181, 191, 193, 197, 199, 211, 223, 227, 229, 233, 239, 241, 251, 257, 263, 269, 271, 277, 281, 283, 293, 307, 311, 313, 317, 331, 337, 347, 349, 353, 359, 367, 373, 379, 383, 389, 397, 401, 409, 419, 421, 431, 433, 439, 443, 449, 457, 461, 463, 467, 479, 487, 491, 499, 503, 509, 521, 523, 541]

# choose randome primes
p = random.choice(primes)
q = random.choice(primes)
# p = 107
# q = 127

print(f"Primes Selected: P = {p}, Q = {q}")

# X value
x = -2

# Hashing with our function
hashed_value = h1(x, p, q)

print(f"Original X = {x}, Hashed value = {hashed_value}")

'''
One Way Property: This does satisfy the One Way Property even if we know n. We because of the Modulus, we don't know how many times the original function has 'wrapped around' so to speak. We can't predict the output.


Weak Collision Resistance: This is NOT Weak Collision Resistant, it is possible to generate the same hash value for two different inputs. We can use -2 and 2 as our input x values and p = 107 and q = 127 for our primes.
    Because of the x**2, they will be the same value N = 13589 when being fed into the mod function and will output the same hash. 
    Because for any two inputs x1 and x2, if x1 ≠ x2, then there exists a possibility that h1(x1) = h1(x2) which means that this is false.


Strong Collision Resistance: This is NOT Strong Collision Resistant. The reason is that for any two inputs x1 and x2, the hash function h1(x) produces the same output if x1 = -x2 (mod n). That is, h1(x1) = h1(x2) if x1 ≡ -x2 (mod n). 
    An attacker who knows the primes p and q can easily find two inputs x1 and x2 such that x1 ≡ -x2 (mod n) and then generate a collision by computing h1(x1) and h1(x2). 



'''