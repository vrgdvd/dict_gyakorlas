'''a=7
print(a)
'''

előadó = []
cím = []
adat1 = None
adat2 = None
 
while len(előadó) != 5:
    adat1 = input('Írj egy előadót!')
    adat2 = input('Írj egy számcímet!')
    előadó.append(adat1)
    cím.append(adat2)
    '''print(előadó, cím)'''

    '''keresés előadó szerint
    keresés cím szerin'''

    if len(előadó) == 5:
        print(előadó, '\n', cím)