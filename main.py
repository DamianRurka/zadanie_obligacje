import sys
#
# klasa = []
# osoba = []
#
# while True:
#     wejscie = input()
#     if wejscie !="":
#         if wejscie == "koniec":
#             if osoba:
#                 klasa.append(osoba)
#             break
#         elif wejscie in ["wychowawca", "nauczyciel", "uczen"]:
#             if not osoba:
#                 osoba.append(wejscie)
#             else:
#                 klasa.append(osoba)
#                 osoba = [wejscie]
#         else:
#             osoba.append(wejscie)
# print(klasa)

class Wychowawca:
    def __init__(self):
        self.name = None
        self.klasy = []

    def wczytaj(self):
        self.name = input()

        while True:
            klasa = input()
            if not klasa:
                break
            self.klasy.append(klasa)

    def wypisz(self):
        print("wychowawca {}, {}".format(self.name, self.klasy))

class Nauczyciel:
    def __init__(self):
        self.name = None
        self.przedmiot = None
        self.klasy = []

    def wczytaj(self):
        self.name = input()
        self.przedmiot = input()

        while True:
            klasa = input()
            if not klasa:
                break
            self.klasy.append(klasa)

    def wypisz(self):
        print("Nauczyciel {}, uczący {}, {}".format(self.name, self.przedmiot, self.klasy))
class Uczen:
    def __init__(self):
        self.name = None
        self.klasa = None

    def wczytaj(self):
        self.name = input()
        self.klasa = input()

    def wypisz(self):
        print("uczen {}, klasa {}".format(self.name, self.klasa))


klasy = {}
uczniowie = []
nauczyciele = []
wychowawcy = []

while True:
    wejscie = input()
    if wejscie == "koniec":
        break
    elif wejscie == "uczen":
        uczen = Uczen()
        uczen.wczytaj()
        uczniowie.append(uczen)
        if uczen.klasa in klasy.keys():
            klasy[uczen.klasa].append(uczen)
        else:
            klasy[uczen.klasa] = [uczen]
    elif wejscie == "wychowawca":
        wychowawca = Wychowawca()
        wychowawca.wczytaj()
        wychowawcy.append(wychowawca)
    elif wejscie == "nauczyciel":
        nauczyciel = Nauczyciel()
        nauczyciel.wczytaj()
        nauczyciele.append(nauczyciel)
    else:
        print("złe dane")
        break

# akcja = sys.argv[1]
#
# if len(akcja) > 2:
#     for osoba in wychowawcy + nauczyciele + uczniowie:
#         if osoba.name == akcja:
#             osoba.wypisz()

print(klasy)