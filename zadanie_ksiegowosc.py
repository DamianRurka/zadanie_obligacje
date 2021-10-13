
import sys

saldo = 0
magazyn = {}

historia = []

while True:
    komenda = []
    akcja = input()
    if akcja == 'stop':
        break
    if akcja == "saldo":
        komenda.append('saldo')
        komenda.append(input())
        komenda.append(input())
        historia.append(komenda)
    elif akcja == "zakup":
        komenda.append('zakup')
        komenda.append(input())
        komenda.append(input())
        komenda.append(input())
        historia.append(komenda)
    elif akcja == "sprzedaz":
        komenda.append('sprzedaz')
        komenda.append(input())
        komenda.append(input())
        komenda.append(input())
        historia.append(komenda)
    else:
        print('niedozwolona akcja' )
        break
komenda = sys.argv[1:]
historia.append(komenda)
for komenda in historia:
    akcja = komenda[0]
    if akcja == 'saldo'and saldo + int(komenda[1]) >= 0:
        saldo+=int(komenda[1])
    elif akcja =='zakup':
        produkt = komenda[1]
        cena = int(komenda[2])
        ilosc = int(komenda[3])
        if saldo >= cena*ilosc:
            saldo -= ilosc * cena
            if magazyn.get(produkt):
               magazyn[produkt] += ilosc
            else:
                magazyn[produkt] = ilosc
        else:
            print('nie stać cię na zakup produktów')
            break
    elif akcja == 'sprzedaz':
        produkt = komenda[1]
        cena = int(komenda[2])
        ilosc = int(komenda[3])
        if magazyn.get(produkt) and magazyn.get(produkt) >= ilosc:
            saldo += ilosc * cena
            magazyn[produkt] -= ilosc
        else:
            print('brak produktów do sprzedazy')
            break
    elif akcja == 'konto':
        print('saldo konta : ', saldo)
    elif akcja == 'magazyn':
        print('stan magazynu: ', magazyn)
    elif akcja == 'przegląd':
        od = int(komenda[2])
        do = int(komenda[3])
        print(historia[od:do])


for komenda in historia:
    for x in komenda:
        print(x)

