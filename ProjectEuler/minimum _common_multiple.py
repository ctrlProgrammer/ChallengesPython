from library.Primes import Primes
from library.MCM import MCM

primes = Primes('utils/primes_array.txt')
primes_array = primes.get_primes_txt()
number_list = []

# Generate number list
for i in range(1, 11):
    number_list.append(i)

mcm = MCM(primes_array)
mcm.get_mcm(number_list)
