## Lista Dinamica Simplesmente Encadeada

class No():
    def __init__(self, valor, proximo):
        self.info = valor
        self.prox = proximo


class FilaD():
    def __init__(self):
        self.__prim = None
        self.__ult = None
        self.__quant = 0

    def inserir(self, valor):
        if self.__quant == 0:
            self.__prim = self.__ult = No(valor, None)
        else:
            self.__ult.prox = self.__ult = No(valor, None)
        self.__quant += 1

    def remover(self):
        if self.__quant == 1:
            self.__prim = self.__ult = None
        else:
            self.__prim = self.__prim.prox
        self.__quant -= 1

    def imprimir(self):
        aux = self.__prim
        texto = ''
        while aux is not None:
            texto += aux.info + '\t'
            aux = aux.prox
        print texto

    def getQuant(self):
        return self.__quant

    def getPrim(self):
        return self.__prim.info
