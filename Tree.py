from No import No


class Tree:
    def __init__(self):
        self.raiz = None

    def insere(self, valor):
        if self.raiz == None:
            self.raiz = No(valor)
        else:
            self.raiz.insere(valor)
            print("?")

    def busca(self, valor):
        if self.raiz == None:
            return False
        else:
            return self.raiz.busca(valor)

    def inOrdem(self):
        if self.raiz != None:
            self.raiz.inOrdem()

    def soma(self):
        if self.raiz != None:
            return self.raiz.soma()

    def somaFolhas(self):
        if self.raiz != None:
            return self.raiz.somaFolhas()

    def printFolhas(self):
        if self.raiz != None:
            self.raiz.printFolhas()

    def altura(self):
        if self.raiz != None:
            return self.raiz.altura()

    def h(self, valor):
        if self.raiz != None:
            return self.raiz.h(valor)

    def nivel(self, valor):
        if self.raiz != None:
            return self.raiz.nivel(valor)

    def maisdir(self):
        if self.raiz != None:
            return self.raiz.maisdir()

    def maisesq(self):
        if self.raiz != None:
            return self.raiz.maisesq()
