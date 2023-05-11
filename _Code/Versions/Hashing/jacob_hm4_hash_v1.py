from Crypto.Util.number import inverse

def factorize(n):
    i = 2
    factors = []
    while i * i <= n:
        if n % i:
            i += 1
        else:
            n //= i
            factors.append(i)
    if n > 1:
        factors.append(n)
    return factors


def h1(x, n):
    return pow(x, 2, n)

def find_collision_h1(n):
    p, q = factorize(n)
    sqrt_h1_x_mod_p = pow(h1(2, p), inverse(2, p+1), p)
    sqrt_h1_x_mod_q = pow(h1(2, q), inverse(2, q+1), q)
    x = (q * inverse(q, p) * sqrt_h1_x_mod_p + p * inverse(p, q) * sqrt_h1_x_mod_q) % n
    y = n - x
    return (x, y)

# Test with some random value of n
n = 88362826219152035846031863753008967849019589330965406564775886169854194512261
print(find_collision_h1(n))
