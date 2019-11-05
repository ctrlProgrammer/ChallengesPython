"""
Creado por CtrlProgrammer
https://github.com/ctrlProgrammer/
"""

import os.path as path


class Primes():
    """
    Validacion y contencion de numeros primos.

    Validacion:
        Se considera numero primo aquel que solo es divisible de manera entera
        entre 1 y el mismo

    Metodo para contener numeros primos:
        Se utiliza un bucle en el que validamos cada numero hasta un maximo
        en el bucle se guardan constantemente los numeros considerados primos
        y se crea una lista con ellos. Despues se crea un archivo .txt en el
        que se almacenan para su proximo uso. De esta manera solo generamos y
        validamos cierta cantidad de numeros primos.
    """

    def __init__(self, primes_txt):
        """
        Se obtiene el nombre del archivo en donde se quieren generar u
        obtener los numeros primos
        """

        self.primes_txt = primes_txt
        self.get_primes_txt()

    def is_prime(self, num):
        """
        Validacion de numeros primos

        Se considera numero primo aquel que solo es divisible de manera entera
        entre 1 y el mismo
        """

        divisors = []

        for i in range(1, num + 1):
            div = num / i

            if(isinstance(div, float)):
                if div.is_integer():
                    div = int(div)

            if isinstance(div, int):
                divisors.append(i)

        "Si este numero solo tiene dos divisores es considerado primo (el mismo y 1)"
        if(len(divisors) == 2):
            return True
        else:
            return False

    def create_primes_array(self, max_prime):
        """
        Generacion de numeros primos

        Genera una lista llena de numeros primos, desde el 1 hasta el maximo 
        incluido en los paramentros
        """

        primes = []
        for i in range(1, max_prime):
            if self.is_prime(i):
                primes.append(i)
        return primes

    def write_primes_txt(self, max_prime):
        """
        Generacion de archivo con numeros primos

        Obtiene la lista de primos, los transforma en un string y los separa con ,
        """

        f = open(self.primes_txt, 'w')
        primes_array = self.create_primes_array(max_prime)
        primes_array = ",".join(str(int_) for int_ in primes_array)
        if f.write(primes_array):
            return True

    def get_primes_txt(self):
        """
        Obtencion de archivo con primos 

        Formato:
            1,3,5,7...

        Abre el archivo y lo convierte en una lista de enteros
        """

        if(path.exists(self.primes_txt)):
            f = open(self.primes_txt)
            primes_array = f.read()

            # Seaparate all element with ,
            primes_array = primes_array.split(',')

            # Convert all elements to integer
            for i in range(0, len(primes_array)):
                primes_array[i] = int(primes_array[i])

            return primes_array
        else:
            self.write_primes_txt(10000)
