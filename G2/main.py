from G2 import Tree

t1 = Tree.Tree()
#t1.insere(4)
#t1.insere(2)
#t1.insere(6)
#t1.insere(7)
#t1.insere(1)
#t1.insere(5)
#t1.insere(3)
# t1.printFolhas()
# t1.inOrdem()
#print(t1.maisesq())
# t1.printFolhas()
t1.insere(2)
t1.insere(1)
t1.insere(4)
t1.insere(3)
t1.insere(5)
t1.insere(6)
print('Pai')
print(t1.retornaPai(5))

def hilbert_curve(n):
    ''' Generate Hilbert curve indexing for (n, n) array. 'n' must be a power of two. '''
    # recursion base
    if n == 1:
        return zeros((1, 1), int32)
    # make (n/2, n/2) index
    t = hilbert_curve(n//2)
    # flip it four times and add index offsets
    a = flipud(rot90(t))
    b = t + t.size
    c = t + t.size*2
    d = flipud(rot90(t, -1)) + t.size*3
    # and stack four tiles into resulting array
    return vstack(map(hstack, [[a, b], [d, c]]))
