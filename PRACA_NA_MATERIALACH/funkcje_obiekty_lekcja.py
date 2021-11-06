
LICZBA_GWIAZDEK = 20


def separator(liczba_gwiazdek = LICZBA_GWIAZDEK ):
    print('-' * liczba_gwiazdek + "FIRMA RURKA" + '-' * liczba_gwiazdek)


def p_kwadrat_ulubionej_liczby(liczba):
    separator()
    print('kwadrat twojej liczby to:, {}! '.format(liczba))
    separator()

def kwadrat_liczby(liczba):
    a = liczba * liczba
    return a

def print_ulubiona_liczba(ulubiona_liczba):
    separator()
    print('Twoja ulubiona liczba to:, {}! '.format(ulubiona_liczba))
    separator()

def print_hello(imie, nazwisko, obywatelstwo=None, kraj_urodzenia=None):
    separator()
    print('Witaj, {} {}! '.format(imie, nazwisko))
    if obywatelstwo:
        print('masz {} obywatelstwo' .format(obywatelstwo))
    if kraj_urodzenia:
        print('pochodzisz z {}'.format(kraj_urodzenia))
    separator()
imie = input()
nazwisko = input()
obywatelstwo=input()
kraj_urodzenia=input()
ulubiona_liczba = input()
print_hello(nazwisko = nazwisko, imie = imie, kraj_urodzenia=kraj_urodzenia )
print_ulubiona_liczba(ulubiona_liczba = ulubiona_liczba)
#
#
#
# # ulubiona_liczba = int(input('podaj liczbe:'))
# # print_ulubiona_liczba(ulubiona_liczba)
# # kwadrat = kwadrat_liczby(ulubiona_liczba)
# # p_kwadrat_ulubionej_liczby(kwadrat)
#


#
# def dodaj_liczbe(liczba):
#     liczba += 5
#     print('2 miejsce: ', liczba)
#     return liczba
# liczba = 10
# print('1 miejsce: ', liczba)
# nowa_liczba = dodaj_liczbe(liczba)
# print('3 miejsce ; ', liczba)
# print('4 miejsce ; ', nowa_liczba)
#
# def dodaj_do_tablicy(tabl, slow):
#     tabl.append(5)
#     print("2 : ",tabl)
#     slow['new'] = 5
#     print("2 : ", slow)
#
#
#
# tabl = [1,2]
# slow = {'old': 2}
# print("1 : ",tabl)
# print("1 : ",slow)
# dodaj_do_tablicy(tabl, slow)
# print("3 : ", tabl)
# print("3 : ", slow)


#
# pare_elementow = (1, 2, 3, 4)
# print(pare_elementow)
# pare_elementow = 1, 2, 3, 4
# print(pare_elementow)



#
# def print_hello(imie, nazwisko):
#     print('Witaj, {} {}! '.format(imie, nazwisko))
#
# print_hello(input(), input())
#
#
# pracownicy = [
#     {
#         'imie': 'damian',
#         'zespol': 'Backend',
#         'pensja podstawowa': '16000'
#      },
#     {
#         'imie': 'staszek',
#         'zespol': 'devOps',
#         'pensja podstawowa': '20000',
#         'uptime': 0.99
#      },
#     {
#         'imie': 'lukasz',
#         'zespol': 'sprzedaz',
#         'pensja podstawowa': '8000',
#         'podpisane kontrakty': 8,
#         'premia od kontraktu': 500}
# ]
#
# TPL= "{} | {}"
#
# def wypisz_pracownika(pracownicy):
#     print(TPL.format(pracownik['imie'], pracownik['zespol']))
#
# def wypisz_pensje_backend(pracownik):
#     print(pracownik['pensja podstawowa'])
#
# def wypisz_pensje_devops(pracownik):
#     pensja = pracownik['pensja podstawowa'] * pracownik['uptime']
#     print("Pensja:", pensja)
#
# def wypisz_pensje_sprzedaz(pracownik):
#     pensja = pracownik['pensja podstawowa'] + pracownik['podpisane kontrakty'] * pracownik['premia od kontraktu']
#     print('Pensja :', pensja)
#
#
# for pracownik in pracownicy:
#     wypisz_pracownika(pracownik)
#     if pracownik['zespol'] == 'Backend':
#         wypisz_pensje_backend(pracownik)
#     if pracownik['zespol'] == 'devOps':
#         wypisz_pensje_devops(pracownik)
#     if pracownik['zespol'] == 'sprzedaz':
#         wypisz_pensje_sprzedaz(pracownik)