f=open("zad4.txt","a")
f.write("Metody\n")
f.write("Inzynieri\n")
f.write("Wiedzy\n")
f.close()

with open("zad4.txt","r") as file:
    for line in file:
        print(line, end="")
