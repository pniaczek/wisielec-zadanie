import random


lista_slow = ['banan', 'ananas', 'arbuz', 'mandarynka']


slowo = lista_slow[random.randrange(0, len(lista_slow))]
print('Słowo które musisz zgadnąć ma', len(slowo),'liter')

i = 0

zuzyte_litery = []

while (True):
    m = 0

    litera = input("\npodaj jedną literę: ")

    for n in range(0, len(zuzyte_litery)):
        if litera == zuzyte_litery[n]:
            m = 1


    if slowo.find(litera) != -1 and m == 0:

        zuzyte_litery.append(litera)

        for p in range(0, len(slowo)):
            if litera == slowo[p]:
                m = m+1

        print("liter", litera, "jest", m, "w zgadywanym słowie")
        i = i+m

    print("zgadłeś już", i, "z", len(slowo), "liter w słowie")

    if i == len(slowo):
        break
