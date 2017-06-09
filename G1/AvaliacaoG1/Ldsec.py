## Lista Dinamica Simplesmente Encadeada

class No():
    def __init__(self, anterior, valor, proximo):
        self.ant = anterior
        self.info = valor
        self.prox = proximo


class Ldsec():
    def __init__(self):
        self.__prim = None
        self.__quant = 0

    def inserirInicio(self, valor):
        if self.__quant == 0:
            self.__prim = No(self.__prim, valor, self.__prim)
            self.__prim.ant = self.__prim
            self.__quant += 1
        else:
            self.__prim = No(self.__prim.ant, valor, self.__prim)
            self.__prim.prox.ant = self.__prim
            self.__quant += 1

    def inserirFim(self, valor):
        if self.__quant == 0:
            self.inserirInicio(valor)
        else:
            aux = self.__prim
            for x in range(self.__quant):
                if x == (self.__quant - 1):
                    aux.prox = No(aux, valor, self.__prim)
                    self.__prim.ant = aux.prox
                aux = aux.prox
            self.__quant += 1

    def removerInicio(self):
        if self.__quant == 1:
            self.__prim = None
        else:
            aux = self.__prim
            self.__prim = self.__prim.prox
            self.__prim.ant = aux.ant
        self.__quant -= 1

    def removerFim(self):
        if self.__quant == 1:
            self.removerInicio()
        else:
            aux = self.__prim
            for x in range(self.__quant):
                if x == (self.__quant - 2):
                    aux.prox = self.__prim
                    self.__prim.ant = aux
                    self.__quant -= 1
                    break
                aux = aux.prox

    def inserirAposDet(self, apos, det):
        aux = self.__prim
        for x in range(self.__quant):
            if aux.info == apos:
                aux.prox = No(aux, det, aux.prox)
                aux.prox.prox.ant = aux.prox
                self.__quant += 1
            aux = aux.prox

    def removerDet(self, det):
        if self.__prim.info == det:
            self.removerInicio()
        elif self.__prim.ant == det:
            self.removerFim()
        aux = self.__prim
        for x in range(self.__quant):
            if aux.info == det:
                aux.ant.prox = aux.prox
                aux.prox.ant = aux.ant
                self.__quant -= 1
            aux = aux.prox

    def imprimir(self):
        aux = self.__prim
        texto = ''
        for x in range(self.__quant):
            texto += aux.info + '\t '
            aux = aux.prox
        print texto

    def imprimirReverso(self):
        aux = self.__prim
        texto = ''
        for x in range(self.__quant):
            aux = aux.ant
            texto += aux.info + '\t '
        print texto

    def getQuant(self):
        return self.__quant

    def getPrim(self):
        return self.__prim.info

    def getUlt(self):
        aux = self.__prim
        for x in range(self.__quant):
            if x == (self.__quant - 1):
                return aux.info
            aux = aux.prox

    def estaVazia(self):
        return self.__quant == 0
