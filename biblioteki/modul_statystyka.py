NAZWA_KRAJU = 'Polska'
def wypisz_liczby(n):
    for idx in range(n):
        print(idx)

class statystyka:
    def __init__(self):
        self.ludnosc = {}

    def wczytaj_ludnosc(self,sciezka):
        with open(sciezka,'r') as f:     #f =skrót od file file=plik
            while True:
                miasto = f.readline().strip()
                if not miasto:
                    return
                ludnosc = f.readline().strip()
                self.ludnosc[miasto] = ludnosc

    def wypisz_ludnosc(self):                  #przykladowe wyniki:
        for k,v in self.ludnosc.items():       #  Malbork : 120000
            print(k,':', v)                    # olsztyn: 50000
     #   print(self.ludnosc)

    def dopisz_miasto(self, nowe_miasto, liczba_ludnosci):
        self.ludnosc[nowe_miasto] = liczba_ludnosci

    def zapisz_do_pliku(self,nazwa_pliku):
        with open(nazwa_pliku, 'w') as f:
            for k,v in self.ludnosc.items():
                f.write(k + '\n')
                f.write(str(v)+ '\n')

    def dopisz_do_pliku(self, sciezka_do_pliku, nazwa_miasta, liczba_ludnosci):
        self.ludnosc[nazwa_miasta] = liczba_ludnosci           #<- bez tej linijki miasto wrocław nie zostanie \
        with open(sciezka_do_pliku, 'a') as f:                 #wyswietlone w terminalu!!!!!!!!!
            f.write(nazwa_miasta + '\n')
            f.write(str(liczba_ludnosci) + '\n')


stat = statystyka()
stat.wczytaj_ludnosc('edytowalne_dane.txt')
stat.dopisz_miasto('gdynia', 250_000)
stat.zapisz_do_pliku('nowy_tekstowy_z_edyt_dane.txt')
stat.dopisz_do_pliku('nowy_tekstowy_z_edyt_dane.txt', 'wroclaw' , 280000)
stat.wypisz_ludnosc()