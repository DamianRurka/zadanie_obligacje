import os
import sys
import csv

src = sys.argv[1]
dst = sys.argv[2]
zmiany = sys.argv[3:]

def obsluga_CSV():
    #python reader.py "PROGRAM_DO_CSV/KATALOG_WEWNETRZNY/lead_shot.csv" "PROGRAM_DO_CSV/NOWY_KATALOG" "1,1,5" "2,2,4"
    if not os.path.isdir(dst):
        print(f'błąd podanej ścieżki {dst} lub podany katalog nie istnieje ')
        os.mkdir(dst)
        print('katalog został utworzony')

    wyzszy_katalog, nazwa_pliku = os.path.split(src)
    if not os.path.isfile(src):
        print(f'błąd nazwy {nazwa_pliku} lub podany plik nie istnieje ')
        print(f"Pliki w katalogu {wyzszy_katalog}:")
        print(os.listdir(wyzszy_katalog))
    else:
        with open(src, 'r') as plik:
            reader = csv.reader(plik, skipinitialspace=True)
            file_data = []
            for wiersz in reader:
                file_data.append(wiersz)
        for zmiana in zmiany:
            z = zmiana.split(',')
            liczba_wierszy = len(file_data)
            liczba_kolumn = len(file_data[0])

            if liczba_wierszy > int(z[0]) and liczba_kolumn > int(z[1]):
                file_data[int(z[0])][int(z[1])]=z[2]

    sciezka_nowego_pliku = os.path.join(dst, nazwa_pliku)
    with open(sciezka_nowego_pliku, 'w') as save_file:
        writer = csv.writer(save_file)
        for linia in file_data:
            writer.writerow(linia)

obsluga_CSV()
