import numpy as np

__author__ = 'zingkg'

def get_primes(num):
    is_prime = np.ones(num, dtype=np.bool)
    for i in range(2, is_prime.size):
        if is_prime[i]:
            j = 2
            while i * j < is_prime.size:
                is_prime[i * j] = False
                j += 1

    primes = []
    for i in range(2, is_prime.size):
        if is_prime[i]:
            primes.append(i)
    return primes
