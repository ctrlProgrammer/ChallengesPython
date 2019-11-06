"""
Creado por CtrlProgrammer
https://github.com/ctrlProgrammer/
"""


class MCM():
    def __init__(self, primes_list):
        self.primes = primes_list

    def validate_one_on_all(self, number_list):
        error = 0
        for i in number_list:
            if i != 1:
                error += 1

        if error == 0:
            return True
        else:
            return False

    def validate_if_prime_work(self, number_list, prime):
        work = 0
        for i in number_list:
            if i % prime == 0:
                work += 1

        if work > 0:
            return True
        else:
            return False

    def get_all_factors(self, number_list):
        new_number_list = number_list
        factors = []
        primes_counter = 0
        bucle = True

        while bucle:

            for i in range(0, len(new_number_list)):

                if (new_number_list[i] % self.primes[primes_counter] == 0):
                    result = int(new_number_list[i]) / \
                        int(self.primes[primes_counter])

                    if(isinstance(result, float)):
                        if result.is_integer():
                            result = int(result)

                    new_number_list[i] = result

            factors.append(self.primes[primes_counter])

            if(self.validate_if_prime_work(new_number_list, self.primes[primes_counter]) == False):
                primes_counter += 1

            if(self.validate_one_on_all(new_number_list)):
                bucle = False

        return factors

    def get_mcm(self, number_list):
        factors = self.get_all_factors(number_list)
        mcm = 1
        for i in factors:
            mcm *= i

        print(mcm)
