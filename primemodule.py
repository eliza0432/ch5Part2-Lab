###Create a new file as primemodule.py that includes the following functions:
# is_prime(n): returns True if n is a prime number, False otherwise
# print_primes(n): prints all prime numbers less than n
# get_primes(n): returns a list of all prime numbers less than n

def is_prime(n):
    if n <=1:
        result = False
    for i in range(2, n):
        if n % i == 0:
            result = False
            break
    else:
        result = True
    return result

def print_primes(n):
    for num in range(2, n):
        if is_prime(num):
            print(num)

def get_primes(n):
    primes = []
    for num in range(2, n):
        if is_prime(num):
            primes.append(num)
    return primes