import LES

L1 = LES.LES()
if L1.estaCheia():
    print('Nao pode')
else:
    L1.inserirInicio('A')
    L1.inserirInicio('B')
    L1.inserirInicio('C')
    L1.inserirFim('D')
    L1.inserirAposDet('E','A')
    L1.printLista()
    L1.removerInicio()
    L1.inserirAposDet('F','B')
    L1.printLista()
    L1.removerFim()
    L1.inserirAposDet('E','D')
    L1.printLista()
print('A lista tem ', L1.getQuant() ,' elementos')
L1.printLista()
