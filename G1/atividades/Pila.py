## Lista Dinamica Simplesmente Encadeada

class No():
    def __init__(self, valor, proximo):
        self.info = valor
        self.prox = proximo


class Pila():
    def __init__(self):
        self.__topo = None
        self.__quant = 0

    def push(self, valor):
        if self.__quant == 0:
            self.__topo = No(valor, None)
        else:
            self.__topo = No(valor, self.__topo)
        self.__quant += 1

    def pop(self):
        if self.__quant == 1:
            self.__topo = None
        else:
            self.__topo = self.__topo.prox
        self.__quant -= 1

    def getTopo(self):
        return self.__topo.info
