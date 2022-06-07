def czySilne(haslo):
    if len(haslo)>=10 and "!" in haslo:
        l = False
        u = False
        for x in haslo:
            if x>='a' and x<='z':
                l=True
            elif x>='A' and x<='Z':
                u=True
            if l and u:
                return True
    return False

print(czySilne("Adam!Zalewski"))
print(czySilne("Adam"))
print(czySilne("Adam!"))
print(czySilne("ADAM"))
print(czySilne("AdamZalewski"))
