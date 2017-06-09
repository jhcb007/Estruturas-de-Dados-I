class FilaE():
    def __init__(self):
        self.__lista = [None, None, None, None, None]
        self.__quant = 0

    def inserir(self, valor):
        self.__lista[self.__quant] = valor
        self.__quant += 1

    def remover(self):
        i = 0
        while i < self.__quant - 1:
            self.__lista[i] = self.__lista[i + 1]
            i += 1
        self.__quant -= 1

    def getQuant(self):
        return self.__quant

    def getPrim(self):
        return self.__prim.infos

    def estaVazia(self):
        return self.__quant == 0

    def imprimir(self):
        i = 0
        aux = ''
        while i < self.__quant:
            aux += self.__lista[i] + ''
            i += 1
        print aux
