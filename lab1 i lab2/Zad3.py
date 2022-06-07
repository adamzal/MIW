def czyNalezy(tab,x):
    i=0
    p=False
    while i<len(tab):
        if x==tab[i]:
            p=True
            break
        i+=1
    return p

l=[1,2,3,99,4]
print(czyNalezy(l,5))