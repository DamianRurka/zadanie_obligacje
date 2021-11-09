# # POWITANIE = input("Witaj:")
# #
# # def print_hello(firstname):
# #   print(POWITANIE.format(firstname))
# #
# # class Point:
# #   def __init__(self, x, y):
# #     self.x = x
# #     self.y = y
# #
# #   def length(self):
# #     return(self.x+self.x + self.y+self.y)
#
# #Praca na pliku edytowalnedane - fikcyjne dane
# # TIPS:
#
# #
# # tekst = file.readline()
# # print('smrodowo', tekst.rstrip())
# # file.close()
# slownik = {}
#
# file = open('edytowalne_dane.txt')
#
# tekst = file.readlines()
# for dane in tekst:
#   print(dane.rstrip())   #TODO: rstrip() czyszczenie zbędnych znaków z listy !!!! np: /n
# tekst = file.readline()
# print(tekst.rstrip())
#
# file.close()
# file = open('edytowalne_dane.txt')
# while True:                 #TODO:PĘTLA : Czytanie całego pliku  póki są w nim dane (każda linia jest wczytywana osobno)
#   miasto = file.readline()
#   if not miasto:
#     break
#   ludnosc = file.readline()
#   slownik[miasto.rstrip()] = ludnosc.rstrip()
# print(slownik)
#
# SUMA = 0
# for idx in slownik.values():
#   SUMA += int(idx)
# print(SUMA)
#   #TODO:SUMOWANIE LICZBY LUDNOŚCI Z PLIKU TXT

#
#  # print(tekst.rstrip().split(','))    #TODO:wartości odziellone przecinkami (do obsługi NP pliku CSV)

# file = open('edytowalne_dane.txt', 'r')
# print(file)
# slownik = {}
# while True:
#   miasto = file.readline()
#   if not miasto:
#     break
#   ludnosc = file.readline()
#   slownik[miasto.rstrip()] = ludnosc.rstrip()
#
# print(slownik)
# file.close()
# # #TODO : ZROBIENIE SLOWNIKA Z DANYCH Z PLIKU TXT , KLUCZ TO MIASTO A JEGO WARTOŚĆ TO LICZBA LUDNOSCI
# kwadrat = ('222222222222')
# kolo = ('ooooooooooooooooo')
# zimno = ('brrrrrrrrrrrrrrr')
# cieplo = ('auuuuuuuuuuuu')
#
# plik = open('test.txt', 'w')    #TODO: <- TEN KOD TWORZY PLIK wyjscie.txt
#
# plik.write(kwadrat + '\n')
# plik.write(kolo + '\n')
# plik.write(zimno + '\n')
# plik.write(cieplo + '\n')     #TODO:TRYB PISANIA DO PLIKU I NADPISYWANIE GO
# plik.close()
#
# with open('wyjscie.txt', 'r') as plik:  #TODO:TRYB AUTOMATYCZNEGO ZAMKNIECIA PLIKU = close() jest zbędny
#     odczyt = plik.readlines()
# print(odczyt)
# euro = 0
# zloto = {}
#
# with open('wyjscie.txt', 'a') as plik:
#     plik.write( 'zloto\n')
#     plik.write('zloto\n')                 #TODO:TRYB DOPISYWANIA DO PLIKU
#


#TODO: WCZYTYWANIE KLAS I FUNKCJI
#TODO:wczytywanie,dodawanie,dopisywanie,tworzenie do pliku za pomocą klas i funkcji
#
# class statystyka:
#     def __init__(self):
#         self.ludnosc = {}
#
#     def wczytaj_ludnosc(self,sciezka):
#         with open(sciezka,'r') as f:     #f =skrót od file file=plik
#             while True:
#                 miasto = f.readline().strip()
#                 if not miasto:
#                     return
#                 ludnosc = f.readline().strip()
#                 self.ludnosc[miasto] = ludnosc
#
#     def wypisz_ludnosc(self):                  #przykladowe wyniki:
#         for k,v in self.ludnosc.items():       #  Malbork : 120000
#             print(k,':', v)                    # olsztyn: 50000
#      #   print(self.ludnosc)
#
#     def dopisz_miasto(self, nowe_miasto, liczba_ludnosci):
#         self.ludnosc[nowe_miasto] = liczba_ludnosci
#
#     def zapisz_do_pliku(self,nazwa_pliku):
#         with open(nazwa_pliku, 'w') as f:
#             for k,v in self.ludnosc.items():
#                 f.write(k + '\n')
#                 f.write(str(v)+ '\n')
#
#     def dopisz_do_pliku(self, sciezka_do_pliku, nazwa_miasta, liczba_ludnosci):
#         self.ludnosc[nazwa_miasta] = liczba_ludnosci           #<- bez tej linijki miasto wrocław nie zostanie \
#         with open(sciezka_do_pliku, 'a') as f:                 #wyswietlone w terminalu!!!!!!!!!
#             f.write(nazwa_miasta + '\n')
#             f.write(str(liczba_ludnosci) + '\n')
#
#
# stat = statystyka()
# stat.wczytaj_ludnosc('edytowalne_dane.txt')
# stat.dopisz_miasto('gdynia', 250_000)
# stat.zapisz_do_pliku('nowy_tekstowy_z_edyt_dane.txt')
# stat.dopisz_do_pliku('nowy_tekstowy_z_edyt_dane.txt', 'wroclaw' , 280000)
# stat.wypisz_ludnosc()


#TODO:Obsługa modułu(klasa/obiekt/funkcja) z innego pliku i obsługa modułu z innego katalogu

from biblioteki.modul_statystyka import statystyka, NAZWA_KRAJU, wypisz_liczby

obiekt_stat = statystyka()
obiekt_stat.wczytaj_ludnosc('edytowalne_dane.txt')
obiekt_stat.wypisz_ludnosc()

print(NAZWA_KRAJU)
print(wypisz_liczby(5))


file = open('edytowalne_dane.txt', 'r')
for line in file:
    print(line.rstrip())
file.close()                     #TODO:ITEROWANIE PO DANYCH BEZ WCZYTYWANIA

# file.read() WCZYTANIE PLIKU <- NIEZALECANE

