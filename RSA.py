from fractions import gcd
from random import randint
from Key import Key
from SieveEratosthenes import get_primes

__author__ = 'zingkg'

def generate_random_key():
    primes = get_primes(10000)
    public_prime_pos = randint(0, len(primes))
    private_prime_pos = randint(0, len(primes))
    while public_prime_pos == private_prime_pos:
        public_prime_pos = randint(0, len(primes))

    return generate_key(primes[public_prime_pos], primes[private_prime_pos])


def generate_key(public_random, private_random):
    modulus = public_random * private_random
    totient_modulus = (public_random - 1) * (private_random - 1)
    key_coprime = coprime(totient_modulus)
    key_multiplicative_inverse = modular_multiplicative_inverse(key_coprime, totient_modulus)
    return Key(modulus, key_coprime, key_multiplicative_inverse)


def coprime(totient_modulus):
    totient_mod_primes = get_primes(totient_modulus)
    for i_prime in totient_mod_primes:
        if gcd(i_prime, totient_modulus) == 1:
            return i_prime
    return 0


def modular_multiplicative_inverse(key_coprime, totient_modulus):
    for i in range(totient_modulus):
        if ((key_coprime * i) % totient_modulus) == 1:
            return i
    return 0
