import Fila

L1 = Fila.Fila()
'''
L1.push('A')
L1.push('S')
L1.push('A')
L1.imprimir()
print '\n'
print L1.getTopo()
L1.pop()
print L1.getTopo()
L1.pop()
print L1.getTopo()
'''


def imprimir(self):
    aux = self.__topo
    texto = ''
    while aux is not None:
        texto += aux.info + '\t'
        aux = aux.prox
    print texto