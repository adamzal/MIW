from lab7 import *
import numpy as np

def Ak_1(A,k):
    if k==0:
        return A
    wynik=np.dot(np.dot(np.transpose(normalizacja(A)),A),normalizacja(A))
    return Ak_1(wynik,k-1)

A=np.array([[2,-1,2],[-2,1,4],[2,4,6]])
print(Ak_1(A,300))