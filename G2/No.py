class No:
    def __init__(self, valor):
        self.info = valor
        self.esq = None
        self.dir = None

    def insere(self, valor):
        if valor <= self.info:
            if self.esq == None:
                self.esq = No(valor)
                # print("*")
            else:
                self.esq.insere(valor)
                # print("+")
        else:
            if self.dir == None:
                self.dir = No(valor)
                # print("-")
            else:
                self.dir.insere(valor)
                # print("#")

    def busca(self, valor):
        if valor == self.info:
            return True
        elif valor <= self.info:
            if self.esq == None:
                return False
            else:
                return self.esq.busca(valor)
        else:
            if self.dir == None:
                return False
            else:
                return self.dir.busca(valor)

    def inOrdem(self):
        if self.esq != None:
            self.esq.inOrdem()
            print(self.info, end=" ")
        if self.dir != None:
            self.dir.inOrdem()

    def soma(self):
        total = self.info
        if self.esq != None:
            total += self.esq.soma()
        if self.dir != None:
            total += self.dir.soma()
        return total

    def somaFolhas(self):
        total = 0
        if self.esq == None and self.dir == None:
            total = self.info
        if self.esq != None:
            total += self.esq.somaFolhas()
        if self.dir != None:
            total += self.dir.somaFolhas()
        return total

    def printFolhas(self):
        if self.esq != None:
            self.esq.printFolhas()
        if self.esq == None and self.dir == None:
            print(self.info, end=" ")
        if self.dir != None:
            self.dir.printFolhas()

    def max(self, a, b):
        if a > b:
            return a
        return b

    def altura(self):
        hesq = hdir = 0
        if self.esq != None:
            hesq = self.esq.altura()
        if self.dir != None:
            hdir = self.dir.altura()
        return 1 + max(hesq, hdir)

    def h(self, valor):
        if valor == self.info:
            return self.altura()
        elif valor <= self.info:
            if self.esq == None:
                return False
            else:
                return self.esq.h(valor)
        else:
            if self.dir == None:
                return False
            else:
                return self.dir.h(valor)

    def nivel(self, valor):
        if valor == self.info:
            return 1
        elif valor <= self.info:
            if self.esq == None:
                return False
            else:
                aux = self.esq.nivel(valor)
                if aux != False:
                    return 1 + aux
                else:
                    return False
        else:
            if self.dir == None:
                return False
            else:
                aux = self.dir.nivel(valor)
                if aux != False:
                    return 1 + aux
                else:
                    return False

    def maisdir(self):
        if self.dir != None:
            return self.dir.maisdir()
        else:
            return self.info

    def maisesq(self):
        if self.esq != None:
            return self.esq.maisesq()
        else:
            return self.info

    def retornaPai(self, valor):
        if valor == self.info:
            return True
        elif valor <= self.info:
            if self.esq == None:
                return None
            else:
                aux = self.esq.retornaPai(valor)
                if aux == True:
                    return self.info
                else:
                    return aux
        else:
            if self.dir == None:
                return None
            else:
                aux = self.dir.retornaPai(valor)
                if aux == True:
                    return self.info
                else:
                    return aux

    def retornaMenorQue(self, valor):
        if self.info == valor:
            if self.esq != None:
                return self.esq.info
            return True
        elif valor <= self.info:
            if self.esq != None:
                aux = self.esq.retornaMenorQue(valor)
                if aux == True and (valor >= self.info):
                    return self.info
                return aux
            return None
        else:
            if self.dir != None:
                aux = self.dir.retornaMenorQue(valor)
                if aux == True and (valor >= self.info):
                    return self.info
                return aux
            return None

    def retornaIrmao(self, valor):
        if self.info == valor:
            return True
        elif valor <= self.info:
            if self.esq != None:
                aux = self.esq.retornaIrmao(valor)
                if aux == True and self.dir != None:
                    return self.dir.info
                return aux
            else:
                return None
        else:
            if self.dir != None:
                aux = self.dir.retornaIrmao(valor)
                if aux == True and self.esq != None:
                    return self.esq.info
                return aux
            else:
                return None
