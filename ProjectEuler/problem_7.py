"""
https: // projecteuler.net/problem = 7
Creado por CtrlProgrammer
By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.
What is the 10 001st prime number?
"""


from library.Primes import Primes

prime = Primes()
prime_counter = 0
moment_prime = 1
counter = 1

while prime_counter != 10001:
    if prime.is_prime(counter):
        moment_prime = counter
        prime_counter += 1
    counter += 1

print(moment_prime)
