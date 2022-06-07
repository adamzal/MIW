import numpy as np
from math import sqrt


def iloczyn_skalarny(w1, w2):
    return np.dot(w1, np.transpose(w2))


def norma(w):
    return sqrt(iloczyn_skalarny(w, w))


def projekcja(u, v):
    return (iloczyn_skalarny(u, v) / iloczyn_skalarny(u, u)) * u


def get_vector(tab,i):
    wynik=[]
    for x in range(len(tab)):
        wynik+=[tab[x][i]]
    return np.array(wynik)


def ortogonalizacja(tab):
    wynik = []
    for x in range(len(tab[0])):
        if x == 0:
            wynik += [get_vector(tab,x)]
        else:
            p = 0
            for y in range(x):
                p += projekcja(wynik[y], get_vector(tab,x))
            wynik += [get_vector(tab,x) - p]
    return np.array(np.transpose(wynik))


def normalizacja(tab):
    wynik = []
    ort = ortogonalizacja(tab)
    for x in range(len(tab[0])):
        wynik += [1 / norma(get_vector(ort,x)) * get_vector(ort,x)]
    return np.array(np.transpose(wynik))

def get_R(A,Q):
    return np.dot(np.transpose(Q),A)

if __name__=="__main__":
    A=np.array([[2,0,1],[0,1,2],[1,2,0]])
    # powinna wygladac tak:
    # A=QR
    # Q - e1,e2,e3
    # A - v1,v2,v3
    # v1 v2
    # [1, 0]
    # [1, 1]
    # [0, 1]
    a=ortogonalizacja(A)
    Q=normalizacja(A)
    print(a)
    print("Q:",Q)
    print(np.dot(get_vector(Q,0),get_vector(Q,1)))
    print(np.dot(np.transpose(Q),Q))
    print("R=QtA: ",get_R(A,Q))