import random

class NumeroAleatorio:
    def __init__(self) -> None:
        pass

    def generarListaAleatoria(self, n):
        self.n = n
        self.random_numbers = [random.randint(1, 10) for _ in range(1, self.n+1)]
        return self.random_numbers
    
    def contarRepetidos(self):
        self.coincidencias = [self.random_numbers.count(num) for num in range(1, self.n+1)] #lista ocurrencias
        x = list(range(1, self.n+1)) # lista serie del 1 al n
        resultados = dict(zip(x, self.coincidencias)) #dict uniendo serie con ocurrencias
        return resultados




'''
# mismo resultado con un solo metodo

class NumeroAleatorio:
    def __init__(self):
        self.n = 0
        self.random_numbers = []
        self.coincidencias = {}

    def generar(self, n):
        self.n = n
        self.random_numbers = [random.randint(1, 10) for _ in range(self.n)]
        self.coincidencias = {num: self.random_numbers.count(num) for num in range(1, self.n + 1)}
        return self.random_numbers, self.coincidencias

'''