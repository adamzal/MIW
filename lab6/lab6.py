import numpy as np
import matplotlib.pyplot as plt

def srednia(wektor):
    return np.dot(wektor, np.ones(len(wektor))) / len(wektor)


def wariancja(wektor):
    roznica = wektor - srednia(wektor)
    return sum(np.transpose(roznica)*roznica)/len(wektor)
    #return np.dot(roznica, roznica) / len(wektor)


def odchylenie(wektor):
    return wariancja(wektor)**0.5


w = [2, 1, 3, 7, 21, 37, 213, 137, 2137]
# print(srednia(w), np.average(w))
# print(wariancja(w), np.std(w) ** 2)
# print(odchylenie(w), np.std(w))

def regresja(tab):
    X = []
    Y = []
    for i in tab:
        X += [[1, i[0]]]
        Y += [i[1]]
    X=np.array(X)
    Y=np.array(Y)
    wynik = np.dot(np.dot(np.linalg.inv(np.dot(np.transpose(X), X)), np.transpose(X)), Y)
    x=np.linspace(-10,10,100)
    y=wynik[0]*x+wynik[1]
    plt.plot(x,y)
    plt.show()

if __name__ == '__main__':
    with open("punkty.dat", "r") as file:
        tab = [list(map(lambda a: float(a), line.split())) for line in file]
    regresja(tab)

