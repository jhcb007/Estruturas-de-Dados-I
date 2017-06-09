class LES():

    def __init__(self):
        self.__lista = [None, None, None, None, None]
        self.__quant = 0

    def getQuant(self):
        return self.__quant

    def inserirInicio(self, valor):
        i = self.__quant
        while i > 0:
            self.__lista[i] = self.__lista[i - 1]
            i -= 1
        self.__lista[0] = valor
        self.__quant += 1

    def inserirFim(self, valor):
        self.__lista[self.__quant] = valor
        self.__quant += 1

    def removerInicio(self):
        i = 0
        while i < self.__quant - 1:
            self.__lista[i] = self.__lista[i + 1]
            i += 1
        self.__quant -= 1

    def removerFim(self):
        self.__quant -= 1

    def estaCheia(self):
        return self.__quant == 5

    def estaVazia(self):
        return self.__quant == 0

    def printLista(self):
        i = 0
        aux = ''
        while i < self.__quant:
            aux += self.__lista[i] + ''
            i += 1
        print aux

    def inserirAposDet(self, apos, det):
        i = 0
        j = self.__quant
        while i < self.__quant:
            if self.__lista[i] == det:
                while j > i:
                    self.__lista[j] = self.__lista[j - 1]
                    j -= 1
                self.__lista[i + 1] = apos
                self.__quant += 1
            i += 1

    def esvaziarLista(self):
        self.__quant == 0
