## Lista Dinamica Simplesmente Encadeada

class No():
    def __init__(self, valor, proximo):
        self.info = valor
        self.prox = proximo


class Ldse():
    def __init__(self):
        self.__prim = None
        self.__ult = None
        self.__quant = 0

    def inserirInicio(self, valor):
        if self.__quant == 0:
            self.__prim = self.__ult = No(valor, None)
        else:
            self.__prim = No(valor, self.__prim)
        self.__quant += 1

    def inserirFim(self, valor):
        if self.__quant == 0:
            self.__prim = self.__ult = No(valor, None)
        else:
            self.__ult.prox = self.__ult = No(valor, None)
        self.__quant += 1

    def removerInicio(self):
        if self.__quant == 1:
            self.__prim = self.__ult = None
        else:
            self.__prim = self.__prim.prox
        self.__quant -= 1

    def removerFim(self):
        if self.__quant == 1:
            self.__prim = self.__ult = None
        else:
            aux = self.__prim
            while aux.prox.prox is not None:
                aux = aux.prox
            self.__ult = aux
            aux.prox = None
            self.__quant -= 1

    def removerDet(self, det):
        aux = self.__prim
        count = 0
        while aux is not None:
            if aux.info == det:
                if det == self.__prim.info:
                    self.removerInicio()
                elif det == self.__ult.info:
                    self.removerFim()
                count += 1
            ant = aux
            aux = aux.prox
            while aux is not None:
                if aux.info == det:
                    ant.prox = aux.prox
                    self.__quant -= 1
                    count += 1
                ant = aux
                aux = aux.prox
        return str(count)

    def imprimir(self):
        aux = self.__prim
        texto = ''
        while aux is not None:
            texto += aux.info + '\t'
            aux = aux.prox
        print texto

# def getQuant(self):

#   def estaVazia(self):

#   def getPrim():
