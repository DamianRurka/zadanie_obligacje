# import sys
#
# script_name = sys.argv[0]
#
# print(f'script name: {sys.argv[0]}')
#
# if script_name != 'lekcja_wbudowane_pakiety_analiza.py':
#     print('blad w nazwie')
#
#
#
# from sys import argv, stdin,stdout #stdin to odpowiednik standardowego wejścia
# script_name = argv[0]
#
# print(f'script name: {argv[0]}')
#
# if script_name != 'lekcja_wbudowane_pakiety_analiza.py':
#     print('blad w nazwie')

#
# from sys import argv, stdin  #stdin to odpowiednik standardowego wejścia
# aga = stdin.readline()
# print(aga)                #a staje się tym co wpiszemy np damian,
# if aga == 'damian':
#     print("masz ładne imię ",aga)
                                        #TODO:aga = stdin.readline() nie działa jak input bo wynik przypisywany
                                        # jest niby do zmiennej aga ale jako tekst do "odczytu" wartość podana jako
                                        # aga nie staje się obiektem którym można posługiwać się w programie
                                        # tak jak to bywa w przypadku inputu lub sys.argv które pozwalają na
                                        # obsługę otrzymanej wartości

 # .strip() - czyszczenie znaków z imporowanego pliku np in.txt
# TPL = 'imie: {}'   #stała zmienna z duzych!!!!!!!

#TODO:OBA PONIZSZE KODY WCZYTUJĄ LINIE Z PLIKU TXT
##while True:
#     inp = input().strip()
#     if inp == 'stop':
#         break
#     print(f'imie: {inp}')
#
#
# with open('wyjscie.txt', 'r') as file:
#     while True:
#         inp = file.readline().strip()
#         if inp == 'stop':
#             break
#         print(f'imie: {inp}')

#TODO: ponizej pobieranie danych ze standardowego wejscia if stdin lub else argv[1]


# if len(argv) > 1 and '.txt' in argv[1]:
#     input_data = open(argv[1])
# else:
#     input_data = stdin
#
# while True:
#     inp = input_data.readline().strip()
#     if inp == 'stop':
#         break
#     print(f'imie: {inp}')
#TODO:UNIWERSALNA FUNKCJA ZAPISUJACA DO PLIKU LUB WYSWIETLAJACA NA TERMINALU PONIZSZYM KODEM
#python lekcja_wbudowane_pakiety_analiza.py < wyjscie.txt >USUN.TXT
#import os
#from sys import argv, stdin,stdout,stderr, platform #stdin to odpowiednik standardowego wejścia
# def print(text):
#     stdout.write(text+'\n')
#
# def wypisz_imiona(rodzaj_wejscia, rodzaj_wyjscia):
#     while True:
#         inp = rodzaj_wejscia.readline().strip()
#         if inp == 'stop':
#             break
#         rodzaj_wyjscia.write(f'imie: {inp}\n')
#
# if len(argv) > 1 and '.txt' in argv[1]:
#     input_data = open(argv[1], 'r')
# else:
#     input_data = stdin
#
# if len(argv) > 2 and '.txt' in argv[2]:
#     output_data = open(argv[2], 'w')
#
# else:
#     output_data = stdout
#
# wypisz_imiona(rodzaj_wejscia=input_data, rodzaj_wyjscia= output_data)
#TODO:std
#TODO:Ponizsze polecenia wpisane do terminala robią nastepujące rzeczy
#python lekcja_wbudowane_pakiety_analiza.py wyswietla oba ponizsze kody w terminalu
#python lekcja_wbudowane_pakiety_analiza.py > in.txt   wyswietla kanal2 w terminalu a "tekst wypisany"
# jako stdout jest przekierowany do pliku in.txt

#
# stdout.write('tekst wypisany...\n')
# stderr.write('kanal2...\n')
# print(platform)


# sys.stdin #deskryptor standardowego wejścia
# sys.stdout #deskryptor standardowego wyjścia
# sys.stderr #deskryptor standardowego wyjścia błędów

 #TODO:PAKIET OS
# os.unlink(path) # usuwanie pliku
# os.getlogin() # zwraca nazwę zalogowanego użytkownika
# os.getpid() # zwraca id obecnego procesu
# os.terminal_size # zwraca tuple (liczba kolumn, liczba wierszy) w obecnie uruchomionym terminalu
# os.getcwd() # zwraca obecny ROBOCZY katalog
# os.mkdir(path) #tworzy katalog pod wskazaną lokalizacją
# os.remove(path) # usuwa plik w podanej lokalizacji
# os.rename(src, dst) # przenosi plik/katalog z lokalizacji src do dst
# os.system(cmd) # wykonuje polecenie tak, jakby było wpisane w shellu


#TODO:TWORZENIE folderu Z POZIOMU PROGRAMU A NIE LINI KOMEND

# import os
# folder_bazowy = 'nowy_folder1'
# plikpy = 'plikpython.py'   #ZOSTANIE UTWORZONY FOLDER A NIE PLIK
# if folder_bazowy not in os.listdir():
#     os.mkdir(folder_bazowy)
#     os.mkdir(plikpy)


#TODO:
# os.remowe("NAZWA PLIKU DO USUNIECIA")
# terrminal size ponizej
#w,h = os.get_terminal_size()
#print('-' * w)
#



#TODO:JSON

import json

slownik = {
    'pies':{
    'owczarek ': 'niemiecki',
    'wiek': 10
    },
    'kot':{
    'tórecki' : 'póchacz',
    'wiek' : 5,
    'ostatnie badanie' : [2021, 10, 10]
    }
}
print(slownik)
zakodowany = json.dumps(slownik)
odkodowany = json.loads(zakodowany)
# print(zakodowany)
print(odkodowany)
#TODO:zapisanie i odczytanie json'a
# with open('pets.json', 'w') as file:
#     json.dump(slownik, file)
#
# with open('pets.json', 'r') as file:
#     odczyt=json.load(file)
# print(odczyt)
#xTODO: PICKLE
#TODO: PIKLOWANIE PLIKÓW I ODCZYTYWANIE ZAPLIKOWANYCH (ZAKODOWANYCH) PLIKÓW plik pets.pkl

# import pickle
#
#
# with open('pets.pkl' , 'wb') as file:
#     pickle.dump(slownik,file)
# with open('pets.pkl' , 'rb') as file:
#     odczyt = pickle.load(file)
#
# print(odczyt)

# TODO:zapiklowanie klasy test plik pets2.pkl
# class Test:
#     def __init__(self, arg1):
#         self.arg1 = arg1
# import pickle as pkl
# test_inst = Test(5)
# with open('pets2.pkl' , 'wb') as file:
#     pkl.dump(test_inst,file)
# with open('pets2.pkl' , 'wb') as file:
#     odczyt = pkl.load(file)
# print(odczyt)            # ten kod wyświetli potoczny 'nr VIN' identyfikator objektu
# print(odczyt.__dict__)   # __dict__ wyświetla najlepszy wynik w terminalu


#TODO: PLIKI CSV

# import csv
#
# zmienna_której_szukasz = []
#
# with open('inp.csv', 'r') as f:
#     reader = csv.reader(f, delimiter=",", quotechar='"', skipinitialspace=True)
#     for linia in reader:
#         # print(linia[-2])    #<-zwróć uwagę na pozycję w której się znajduje wartość której szukasz
#         if linia[-2] == 'nazwa_zmiennej_której_szukasz w csv':  #<-zwróć uwagę w jaki sposób jest zapisana warość
#             wyczyszczona_linia = []                        #której szukasz przykład ' "sprigifeld"'
#             for element in linia:                           # uwazaj na spacje i rózne znaczniki i separatory
#                 wyczyszczona_linia.append(element.strip())
#             zmienna_której_szukasz.append(wyczyszczona_linia)
#             print(linia)
# #print(zmienna_której_szukasz[-1])
# #zmienna_której_szukasz.append(['wklej tu otrzymany wynik z terminala jesli chcesz dodac jakis specjalny znak'])
# with open('nazwa_pliku_do_którego_zapiszesz_szukane_wartości.csv', 'w') as file:
#     writer = csv.writer(file, delimiter=";",quotechar="|")
#     for wiersz in zmienna_której_szukasz:
#         writer.writerow(wiersz)


#TODO: Biblioteka Math funkcje matematyczne
import math
a = (math.fsum([-5,-5,-5,-5,-5,-5]))
print(a)
print(abs(a))

#wyniki -30.0 i 30.0 abs nie robi odwrotności liczby , usuwa znak poprzedzający wynik (  -  )
#bądz robi odwrotnosc ale tylko w przypadku z liczb ujemnych na dodatnie


#TODO: RE CZYSZCZENIE LINKÓW, TEKSTÓW ITP

import re
text = "#123http://goggle.com"
text2 = "#123http://goggle.com"
print(re.sub('http://', '', text))
print(re.sub('[^a-zA-Z\.:/]', '', text))