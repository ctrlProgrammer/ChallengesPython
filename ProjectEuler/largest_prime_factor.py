"""
https: // projecteuler.net/problem = 3
The prime factors of 13195 are 5, 7, 13 and 29.
What is the largest prime factor of the number 600851475143 ?
cual es el numero primo mas cercano a 600851475143

Creado por CtrlProgrammer
"""

import os.path as path
from time import time
from library.Primes import Primes


def get_first_factor(num, primes):
    get = True
    counter = 0
    while get:
        counter += 1
        if(num % primes[counter] == 0):
            get = False

    return primes[counter]


primes = Primes('utils/primes_array.txt')
primes_array = primes.get_primes_txt()

bucle = True
num = 13195
factors = []

while bucle:
    factor = get_first_factor(num, primes_array)
    factors.append(factor)
    num = num / factor
    if(num == 1):
        bucle = False

print(factors)
