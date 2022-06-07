from math import sqrt
import numpy as np
import random


def metryka(tab1, tab2):
    wynik = 0
    for i in range(len(tab1)):
        wynik += (tab1[i] - tab2[i]) ** 2
    return sqrt(wynik)


def metryka2(tab1, tab2, d=False):
    tab1 = np.array(tab1)
    tab2 = np.array(tab2)
    if not d:
        tab1 = tab1[:len(tab1) - 1]
        tab2 = tab2[:len(tab2) - 1]
    c = tab1-tab2
    wynik = np.dot(c,c)
    return sqrt(wynik)


def grupowanie(tab, index1, index2):
    wynik = dict()
    for x in range(len(tab)):
        pom = tab[x][index1]
        if pom in wynik.keys():
            # wynik[pom].append(metryka(tab[index2], tab[x]))
            wynik[pom].append(metryka2(tab[index2], tab[x]))
        else:
            # wynik[pom] = [metryka(tab[index2], tab[x])]
            wynik[pom] = [metryka2(tab[index2], tab[x])]
    return wynik


def grupowanie1(x, tab):
    wynik = []
    for i in range(len(tab)):
        #wynik.append((tab[i][len(tab[i]) - 1], metryka(x, tab[i])))
        wynik.append((tab[i][len(tab[i]) - 1], metryka2(x, tab[i][:14])))
    return wynik


def grupowanie2(tab):
    wynik = dict()
    for x in range(len(tab)):
        pom = tab[x][0]
        if pom not in wynik.keys():
            wynik[pom] = []
        wynik[pom].append(tab[x][1])
        wynik[pom].sort()
    return wynik


def odleglosc_klasy(tab, k):
    wynik = dict()
    for x in tab.keys():
        suma=0
        for i in range(k):
            suma += tab[x][i]
        if x not in wynik.keys():
            wynik[x] = []
        wynik[x].append(suma)
    return wynik


def knn(x, lista, k):
    p = odleglosc_klasy(grupowanie2(grupowanie1(x, lista)), k)
    wynik = list(p.keys())[0]
    pom1 = list(p.values())
    pom2 = p[0]
    for i in range(len(pom1)):
        if pom1[i] < pom2:
            wynik = list(p.keys())[i]
            pom2 = pom1[i]
    for i in range(len(pom1)):
        if wynik != i and pom2 == pom1[i]:
            wynik = None
    return wynik


def knn2(x, lista, k):
    dic = grupowanie2(grupowanie1(x, lista))
    for i in dic.keys():
        print(dic[i])

def srodek(lista):
    print(lista)


if __name__ == '__main__':
    with open("australian.dat", "r") as file:
        tab = [list(map(lambda a: float(a), line.split())) for line in file]

    print(grupowanie(tab, 14, 0))
    print(tab)
    x = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
    print(grupowanie1(x, tab))
    print(grupowanie2(grupowanie1(x, tab)))
    print(odleglosc_klasy(grupowanie2(grupowanie1(x, tab)), 5))
    y = [1.0, 22.08, 11.46, 2.0, 4.0, 4.0, 1.585, 0.0, 0.0, 0.0, 1.0, 2.0, 100.0, 1213.0]
    print(knn(y, tab, 5))
    print(metryka2(x,y))
    srodek(grupowanie(tab,14,0))
