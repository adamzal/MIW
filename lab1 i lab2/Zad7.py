def roz(tab,r):
    wynik=[]
    for x in tab:
        if x.endswith(r):
            wynik+=[x]
    return wynik

def gen(tab,r):
    for x in tab:
        if x.endswith(r):
            yield x


l=["zad4.txt","zad3.py","zad2.png","zad1.cpp","zad5.txt","zad6.py"]
print(roz(l,"txt"))
print(list(gen(l,"txt")))