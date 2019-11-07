"""
https: // projecteuler.net/problem = 5
2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.
What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?
Creado por CtrlProgrammer
"""

from library.Primes import Primes
from library.MCM import MCM

primes = Primes()
primes_array = primes.get_primes_txt('utils/primes_array.txt')
number_list = []

# Generate number list
for i in range(1, 11):
    number_list.append(i)

mcm = MCM(primes_array)
mcm.get_mcm(number_list)
