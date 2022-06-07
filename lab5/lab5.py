import numpy as np
import matplotlib.pyplot as plt


def fu(x):
    return x

# Całka Monte-Carlo
def calka1(a, b, f, i=100):
    punkty_wewnatrz = 0
    x = np.linspace(a, b, i)
    p = []
    for k in x:
        p += [f(k)]
    y = np.linspace(min(p), max(p), i)
    pole_prostokata = (abs(a) + abs(b)) * (abs(min(p)) + abs(max(p)))
    for i in range(len(x)):
        for j in range(len(y)):
            if f(x[i])>0 and y[j]>0:
                if f(x[i])>=y[j]:
                    punkty_wewnatrz+=1
            elif f(x[i])<0 and y[j]<0:
                if f(x[i])<=y[j]:
                    punkty_wewnatrz-=1
    return pole_prostokata * (punkty_wewnatrz / (len(x) * len(y)))


def plotc1(a, b, f, i=100):
    x = np.linspace(a, b, i)
    y = []
    for k in range(len(x)):
        if x[k]<0:
            y += [-calka1(x[k], 0, f, i)]
        else:
            y+=[calka1(0, x[k], f, i)]
    plt.plot(x, y)
    plt.plot(x, f(x))
    plt.ylim((a, b))
    plt.show()

# Metoda prostokątów
def calka2(a, b, f, i=100):
    suma = 0
    x = np.linspace(a, b, i)
    for k in range(1, len(x)):
        suma += (x[k] - x[k - 1]) * f(x[k])
    return suma


def plotc2(a, b, f, i=100):
    x = np.linspace(a, b, i)
    y = []
    for k in range(len(x)):
        y += [calka2(0, x[k], f, i)]
    plt.plot(x, y)
    plt.plot(x, f(x))
    plt.ylim((a, b))
    plt.show()

# Metoda trapezów
def calka3(a, b, f, i=100):
    suma = 0
    x = np.linspace(a, b, i)
    h = (b - a) / i
    suma += 0.5 * (f(x[0]) + f(x[len(x) - 1]))
    for k in range(1, len(x) - 1):
        suma += f(x[k])
    return h * suma


def plotc3(a, b, f, i=100):
    x = np.linspace(a, b, i)
    y = []
    for k in range(len(x)):
        y += [calka3(0, x[k], f, i)]
    plt.plot(x, y)
    plt.plot(x, f(x))
    plt.ylim((a, b))
    plt.show()

# Metoda Simpsona
def calka4(a, b, f, i=100):
    suma = 0
    x = np.linspace(a, b, i)
    h = (b - a) / i
    suma += f(x[0]) + f(x[len(x) - 1])
    for k in range(1, len(x) - 1):
        if k % 2 == 1:
            suma += 4 * f(x[k])
        else:
            suma += 2 * f(x[k])
    return h / 3 * suma


def plotc4(a, b, f, i=100):
    x = np.linspace(a, b, i)
    y = []
    for k in range(len(x)):
        y += [calka4(0, x[k], f, i)]
    plt.plot(x, y)
    plt.plot(x, f(x))
    plt.ylim((a, b))
    plt.show()

a=0
b=1
c=-5
d=5
print(calka1(a, b, fu))
plotc1(c, d, fu)
print(calka2(a, b, fu))
plotc2(c, d, fu)
print(calka3(a, b, fu))
plotc3(c, d, fu)
print(calka4(a, b, fu))
plotc4(c, d, fu)
