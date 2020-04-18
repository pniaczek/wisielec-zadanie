import random
import sys


lista_slow = ['banan', 'ananas', 'arbuz', 'mandarynka']


slowo = lista_slow[random.randrange(0, len(lista_slow))]
print('Słowo które musisz zgadnąć ma', len(slowo),'liter')
i = 0
m = 0
zuzyte_litery=[]

while (True):
    m = 0
    l = 0
    litera = input("podaj jedną literę: ")

    for n in range(0, len(zuzyte_litery)):
        if litera == zuzyte_litery[n]:
            m = 1

        print("nm")
    if slowo.find(litera) != -1 and m == 0:

        zuzyte_litery.append(litera)

        for p in range(0, len(slowo)):
            if litera == slowo[p]:
                m=m+1

        i = i+m
    print(i)

    if(i==len(slowo)):
        break








