maksymalna_waga_paczki = 20
maksymalna_waga_elementu = 10
min_waga_elementu = 1
liczba_wyslanych_przesylek = 0
waga_elementu = ""
aktualna_waga = 0
puste_kilogramy = 0
numer_paczki  = 0
suma_pustych_kilogramów = 0
liczba_wysłanych_kilogramów = 0
waga_najlzejszej_paczki = 20
numer_najlzejszej_paczki = 0
max_liczba_elementów = int(input("podaj maksymalną liczbę"
                                 " elementów do wysłania :"))
for idx in range(max_liczba_elementów):
    waga_elementu = int(input("podaj wage elementu :"))
    if waga_elementu == 0:
        break
    elif waga_elementu < min_waga_elementu or waga_elementu > maksymalna_waga_elementu:
        print("waga elementu jest nieprawidłowa")
        break
    else:
        liczba_wysłanych_kilogramów += waga_elementu
        if aktualna_waga + waga_elementu <= maksymalna_waga_paczki:
            aktualna_waga += waga_elementu
        else:
            numer_paczki += 1

            if aktualna_waga < waga_najlzejszej_paczki:
                waga_najlzejszej_paczki = aktualna_waga
                numer_najlzejszej_paczki = numer_paczki
            aktualna_waga = waga_elementu

if max_liczba_elementów == 0:
    print("liczba paczek to 0")
else:
    numer_paczki += 1
if aktualna_waga < waga_najlzejszej_paczki:
    waga_najlzejszej_paczki = aktualna_waga
    numer_najlzejszej_paczki = numer_paczki




puste_kilogramy = numer_paczki * 20 - liczba_wysłanych_kilogramów
puste_kilogramy_najlzejsza = 20 - waga_najlzejszej_paczki
if numer_najlzejszej_paczki == 0:
    puste_kilogramy_najlzejsza = 0


print("liczba paczek wysłąnych to :{}.\nliczba wysłanych kilogramów : {}.\n"
      "Suma pustych kilogramów :{}.\nNumer najlzejszej paczki: {}.jest tam {}.pustych kilogramów "
      "".format(numer_paczki, liczba_wyslanych_przesylek, puste_kilogramy,
                numer_najlzejszej_paczki, puste_kilogramy_najlzejsza))




