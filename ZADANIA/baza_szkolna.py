import sys

class Wychowawca:
    def __init__(self):
        self.name = None
        self.klasy = []
        self.uczniowie_wychowawcy = []

    def wczytaj(self):
        self.name = input()

        while True:
            klasa = input()
            if not klasa:
                break
            self.klasy.append(klasa)
    def uczniowie(self):
        imie = input()
        klasa_ucznia = input()
        if klasa_ucznia in self.klasy:
            self.uczniowie_wychowawcy.append(imie)
        print("uczniowie ktorych uczy:", self.uczniowie_wychowawcy)

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

akcja = sys.argv[1]

if len(akcja) > 2:
    for osoba in wychowawcy:
        if akcja == osoba.name:
            osoba.wypisz()
            for uczen in uczniowie:
                if uczen.klasa in osoba.klasy:
                    uczen.wypisz()
    for osoba in nauczyciele:
        if akcja == osoba.name:
            osoba.wypisz()
            for wychowawca in wychowawcy:
                klasy_wspolne = (set(wychowawca.klasy) & set(osoba.klasy))
                if klasy_wspolne:
                    wychowawca.wypisz()
    for uczen in uczniowie:
        if akcja == uczen.name:
            uczen.wypisz()
            for nauczyciel in nauczyciele:
                if uczen.klasa in nauczyciel.klasy:
                    nauczyciel.wypisz()

else:
    for wychowawca in wychowawcy:
        if akcja in wychowawca.klasy:
            wychowawca.wypisz()
    for uczen in uczniowie:
        if akcja == uczen.klasa:
            uczen.wypisz()


#print(klasy)