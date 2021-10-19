import sys

klasa = []
osoba = []

while True:
    wejscie = input()
    if wejscie !="":
        if wejscie == "koniec":
            if osoba:
                klasa.append(osoba)
            break
        elif wejscie in ["wychowawca", "nauczyciel", "uczen"]:
            if not osoba:
                osoba.append(wejscie)
            else:
                klasa.append(osoba)
                osoba = [wejscie]
        else:
            osoba.append(wejscie)
print(klasa)


class Wychowawca:
    def __init__(self, name, klasy):
        self.name = name
        self.klasy = klasy


class Nauczyciel:
    def __init__(self, name, przedmiot, klasy):
        self.name = name
        self.przedmiot = przedmiot
        self.klasy = klasy


class Uczen:
    def __init__(self, name, klasa):
        self.name = name
        self.klasa = klasa
uczniowie = []
nauczyciele = []
wychowawcy = []
while True:
    wejscie = input()
    if wejscie == "koniec":
        break
    elif wejscie == "uczen":
        imie_nazwisko = input()
        klasa = input()
        uczen = Uczen(imie_nazwisko, klasa)
        uczniowie.append(uczen)
    elif wejscie == "wychowawca":
        imie_nazwisko = input()
        klasy = []
        while True:
            klasa = input()
            if not klasa:
                break
            klasy.append(klasa)
        wychowawca = wychowawca(imie_nazwisko, klasy)
        wychowawcy.append(wychowawca)
    elif wejscie == "nauczyciel":
        imie_nazwisko = input()
        przedmiot = input()
        klasy = []
        while True:
            klasa = input()
            if not klasa:
                break
            klasy.append(klasa)
        nauczyciel = Nauczyciel(imie_nazwisko, przedmiot, klasy)
        nauczyciele.append(nauczyciel)
    else:
        print("złe dane")
        break

