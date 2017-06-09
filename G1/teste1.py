# removerDet(self, valor)
# remover todas as ocorrencias de valor da lista e retorna a quantidade

import Ldse

L1 = Ldse.Ldse()
L1.inserirFim('A')
L1.inserirFim('B')
L1.inserirFim('C')
L1.inserirFim('A')
L1.inserirFim('D')
L1.inserirInicio('D')
L1.inserirInicio('A')
L1.imprimir()
#print L1.removerDet('A')
#print L1.removerDet('D')
#print L1.removerDet('C')
print L1.removerDet('B')
L1.imprimir()
