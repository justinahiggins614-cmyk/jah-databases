"""Demo program for the Prime Number Generator Database (prime-number-generator).
Run: python3 demo-prime-number-generator.py
"""
def is_prime(n):
    if n < 2:
        return False
    d = 2
    while d * d <= n:
        if n % d == 0:
            return False
        d += 1
    return True
n = 7
divs = [d for d in range(1, n + 1) if n % d == 0]
print(f"{n} is prime: its only divisors are {divs[0]} and {divs[1]}")
