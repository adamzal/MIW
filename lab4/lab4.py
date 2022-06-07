# kolorowanie punktów
# losowe kolorowanie
# w srodku kropka ma najblizej do wszystkich
# waga kropki = kropka  i lista kropek <- suma odległości
# srodek masy <- kropka
# kropke porownac z odleglosciami do srodow mas

import random
import numpy as np
from math import sqrt

def metryka(tab1, tab2, d=False):
    tab1 = np.array(tab1)
    tab2 = np.array(tab2)
    if not d:
        tab1 = tab1[:len(tab1) - 1]
        tab2 = tab2[:len(tab2) - 1]
    c = tab1-tab2
    wynik = np.dot(c,c)
    return sqrt(wynik)

def losowe(tab):
    for x in range(len(tab)):
        tab[x][14] = random.randint(0, 1)


def grupowanie(tab) -> dict:
    wynik = []
    for x in range(len(tab)):
        l=dict()
        for y in range(len(tab)):
            pom = tab[x][14]
            if pom in l.keys():
                l[pom].append(metryka(tab[y], tab[x]))
            else:
                l[pom] = [metryka(tab[y], tab[x])]
        l["sum"]=sum(l[pom])
        wynik+=[l]
    return wynik

def porownaj(tab, index):
    wynik=False
    for x in range(len(tab)):
        if x!=index[0]:
            m0=metryka(tab[x],tab[index[0]])
        if x!=index[1]:
            m1=metryka(tab[x],tab[index[1]])
        if m0>m1:
            tab[x][14]=1
            wynik=True
        if m0<m1:
            tab[x][14]=0
            wynik=True
    return wynik

def min_index(tab):
    index_0 = 0
    index_1 = 0
    wynik_0=tab[index_0]["sum"]
    wynik_1 = tab[index_1]["sum"]
    for x in range(len(tab)):
        if 0 in tab[x].keys() and tab[x]["sum"]<wynik_0:
            index_0 = x
            wynik_0=tab[index_0]["sum"]
        elif 1 in tab[x].keys() and tab[x]["sum"]<wynik_1:
            index_1 = x
            wynik_1=tab[index_1]["sum"]
    return index_0, index_1


if __name__ == '__main__':
    with open("australian.dat", "r") as file:
        tab = [list(map(lambda a: float(a), line.split())) for line in file]
    tab2= tab.copy()

    p=True
    i=1
    losowe(tab)
    while p:
        a = grupowanie(tab)
        ind=min_index(a)
        p=porownaj(tab,ind)
        if i==5:
            break
        i+=1

    for x in range(len(tab)):
        if tab[x][14]!=tab2[x][14]:
            print(tab[x][14], tab2[x][14])

