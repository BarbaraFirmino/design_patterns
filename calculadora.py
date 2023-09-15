import random


class Calculator():
    def __init__(self, c) -> None:
        self.c = c
        self._c2 = 20
        self.__c3 = 30

    def soma_instancia(self, a, b):
        return a+b+self.c
    
    def soma_classe(a,b):
        return a+b
    
    def _multiplicacao(self, a,b):
        res = a*b
        r = random.random()*10
        soma = self.soma_instancia(res, r)
    
    def __divisao(self, a,b):
        return a/b+self.__c3
    
calc = Calculator(10)
print(calc.soma_instancia(1,2))
calc.c = 20
print(calc.soma_instancia(1,2))

calc2 = Calculator(100)
print(calc2.soma_instancia(1,2))
print(Calculator.soma_classe(1,2))

print(calc2._multiplicacao(2,3))
