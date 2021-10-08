
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
    for x in komenda:
        print(x)
print('stop')
print(historia[0])

