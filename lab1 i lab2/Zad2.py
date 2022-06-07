l=[1,2,3,99,4]
for x in l:
    if x==99:
        continue
    print(x)

for x in l:
    if x!=99:
        print(x)
