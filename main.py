# # Zadanie domowe obligacje
# Styczen = 1.5928244844
# Luty = -0.4535091012
# Marzec = 2.3246717171
# Kwiecien = 1.2612544072
# Maj = 1.7825262857
# Czerwiec = 2.3293845415
# Lipiec = 1.5022298422
# Sierpien = 1.7825262857
# Wrzesien = 2.3288489941
# Pazdziernik = 0.6169213482
# Listopad = 2.3522958864
# Grudzien = 0.3377795452
# Styczen_2 = 1.5770352473
# Luty_2 = -0.2927814426
# Marzec_2 = 2.4861965902
# Kwiecien_2 = 0.2671103178
# Maj_2 = 1.4179526723
# Czerwiec_2 = 1.0542432673
# Lipiec_2 = 1.4805201045
# Sierpien_2 = 1.5770352473
# Wrzesien_2 = -0.0774206903
# Pazdziernik_2 = 1.1657333987
# Listopad_2 = -0.4041867176
# Grudzien_2 = 1.4997085208
# # zmienne  inflacja poszczególnych miesięcy
#
#
# kwota_kredytu = float(input("podaj kwote kredytu: "))
# wysokosc_oprocentowania = float(input('podaj wysokosc oprocentowania: '))
# wysokosc_raty = float(input('podaj wysokosc raty: '))
#
# tekst = '\nTwoja pozostala kwota kredytu w {} to {}.\nTo o {} mniej niż w porzednim miesiacu.'
# print("wciskaj enter by zobaczyć tekst")
#
# input('wcisnij enter')
# inflacja = Styczen
# pozostalo_kredytu = (1 + ((inflacja + wysokosc_oprocentowania) / 1200)) * kwota_kredytu - wysokosc_raty
# print(tekst.format("styczen", round(pozostalo_kredytu, 2), round(kwota_kredytu - pozostalo_kredytu, 2)), end=" ")
# kwota_kredytu = pozostalo_kredytu
#
# input('wcisnij enter')
# inflacja = Luty
# pozostalo_kredytu = (1 + ((inflacja + wysokosc_oprocentowania) / 1200)) * kwota_kredytu - wysokosc_raty
# print(tekst.format("luty", round(pozostalo_kredytu, 2), round(kwota_kredytu - pozostalo_kredytu, 2)), end=" ")
# kwota_kredytu = pozostalo_kredytu
#
# input('wcisnij enter')
# inflacja = Marzec
# pozostalo_kredytu = (1 + ((inflacja + wysokosc_oprocentowania) / 1200)) * kwota_kredytu - wysokosc_raty
# print(tekst.format("marzec", round(pozostalo_kredytu, 2), round(kwota_kredytu - pozostalo_kredytu, 2)), end=" ")
# kwota_kredytu = pozostalo_kredytu
#
# input('wcisnij enter')
# inflacja = Kwiecien
# pozostalo_kredytu = (1 + ((inflacja + wysokosc_oprocentowania) / 1200)) * kwota_kredytu - wysokosc_raty
# print(tekst.format("kwiecień", round(pozostalo_kredytu, 2), round(kwota_kredytu - pozostalo_kredytu, 2)), end=" ")
# kwota_kredytu = pozostalo_kredytu
#
# input('wcisnij enter')
# inflacja = Maj
# pozostalo_kredytu = (1 + ((inflacja + wysokosc_oprocentowania) / 1200)) * kwota_kredytu - wysokosc_raty
# print(tekst.format("maj", round(pozostalo_kredytu, 2), round(kwota_kredytu - pozostalo_kredytu, 2)), end=" ")
# kwota_kredytu = pozostalo_kredytu
#
# input('wcisnij enter')
# inflacja = Czerwiec
# pozostalo_kredytu = (1 + ((inflacja + wysokosc_oprocentowania) / 1200)) * kwota_kredytu - wysokosc_raty
# print(tekst.format("czerwiec", round(pozostalo_kredytu, 2), round(kwota_kredytu - pozostalo_kredytu, 2)), end=" ")
# kwota_kredytu = pozostalo_kredytu
#
# input('wcisnij enter')
# inflacja = Lipiec
# pozostalo_kredytu = (1 + ((inflacja + wysokosc_oprocentowania) / 1200)) * kwota_kredytu - wysokosc_raty
# print(tekst.format("lipiec", round(pozostalo_kredytu, 2), round(kwota_kredytu - pozostalo_kredytu, 2)), end=" ")
# kwota_kredytu = pozostalo_kredytu
#
# input('wcisnij enter')
# inflacja = Sierpien
# pozostalo_kredytu = (1 + ((inflacja + wysokosc_oprocentowania) / 1200)) * kwota_kredytu - wysokosc_raty
# print(tekst.format("sierpień", round(pozostalo_kredytu, 2), round(kwota_kredytu - pozostalo_kredytu, 2)), end=" ")
# kwota_kredytu = pozostalo_kredytu
#
# input('wcisnij enter')
# inflacja = Wrzesien
# pozostalo_kredytu = (1 + ((inflacja + wysokosc_oprocentowania) / 1200)) * kwota_kredytu - wysokosc_raty
# print(tekst.format("wrzesien", round(pozostalo_kredytu, 2), round(kwota_kredytu - pozostalo_kredytu, 2)), end=" ")
# kwota_kredytu = pozostalo_kredytu
#
# input('wcisnij enter')
# inflacja = Pazdziernik
# pozostalo_kredytu = (1 + ((inflacja + wysokosc_oprocentowania) / 1200)) * kwota_kredytu - wysokosc_raty
# print(tekst.format("pazdziernik", round(pozostalo_kredytu, 2), round(kwota_kredytu - pozostalo_kredytu, 2)), end=" ")
# kwota_kredytu = pozostalo_kredytu
#
# input('wcisnij enter')
# inflacja = Listopad
# pozostalo_kredytu = (1 + ((inflacja + wysokosc_oprocentowania) / 1200)) * kwota_kredytu - wysokosc_raty
# print(tekst.format('listopad', round(pozostalo_kredytu, 2), round(kwota_kredytu - pozostalo_kredytu, 2)), end=" ")
# kwota_kredytu = pozostalo_kredytu
#
# input('wcisnij enter')
# inflacja = Grudzien
# pozostalo_kredytu = (1 + ((inflacja + wysokosc_oprocentowania) / 1200)) * kwota_kredytu - wysokosc_raty
# print(tekst.format('grudzien', round(pozostalo_kredytu, 2), round(kwota_kredytu - pozostalo_kredytu, 2)), end=" ")
# kwota_kredytu = pozostalo_kredytu
#
# input('wcisnij enter')
# inflacja = Styczen_2
# pozostalo_kredytu = (1 + ((inflacja + wysokosc_oprocentowania) / 1200)) * kwota_kredytu - wysokosc_raty
# print(tekst.format("styczen_2", round(pozostalo_kredytu, 2), round(kwota_kredytu - pozostalo_kredytu, 2)), end=" ")
# kwota_kredytu = pozostalo_kredytu
#
# input('wcisnij enter')
# inflacja = Luty_2
# pozostalo_kredytu = (1 + ((inflacja + wysokosc_oprocentowania) / 1200)) * kwota_kredytu - wysokosc_raty
# print(tekst.format("luty_2", round(pozostalo_kredytu, 2), round(kwota_kredytu - pozostalo_kredytu, 2)), end=" ")
# kwota_kredytu = pozostalo_kredytu
#
# input('wcisnij enter')
# inflacja = Marzec_2
# pozostalo_kredytu = (1 + ((inflacja + wysokosc_oprocentowania) / 1200)) * kwota_kredytu - wysokosc_raty
# print(tekst.format("marzec_2", round(pozostalo_kredytu, 2), round(kwota_kredytu - pozostalo_kredytu, 2)), end=" ")
# kwota_kredytu = pozostalo_kredytu
#
# input('wcisnij enter')
# inflacja = Kwiecien_2
# pozostalo_kredytu = (1 + ((inflacja + wysokosc_oprocentowania) / 1200)) * kwota_kredytu - wysokosc_raty
# print(tekst.format("kwiecień_2", round(pozostalo_kredytu, 2), round(kwota_kredytu - pozostalo_kredytu, 2)), end=" ")
# kwota_kredytu = pozostalo_kredytu
#
# input('wcisnij enter')
# inflacja = Maj_2
# pozostalo_kredytu = (1 + ((inflacja + wysokosc_oprocentowania) / 1200)) * kwota_kredytu - wysokosc_raty
# print(tekst.format("maj_2", round(pozostalo_kredytu, 2), round(kwota_kredytu - pozostalo_kredytu, 2)), end=" ")
# kwota_kredytu = pozostalo_kredytu
#
# input('wcisnij enter')
# inflacja = Czerwiec_2
# pozostalo_kredytu = (1 + ((inflacja + wysokosc_oprocentowania) / 1200)) * kwota_kredytu - wysokosc_raty
# print(tekst.format("czerwiec_2", round(pozostalo_kredytu, 2), round(kwota_kredytu - pozostalo_kredytu, 2)), end=" ")
# kwota_kredytu = pozostalo_kredytu
#
# input('wcisnij enter')
# inflacja = Lipiec_2
# pozostalo_kredytu = (1 + ((inflacja + wysokosc_oprocentowania) / 1200)) * kwota_kredytu - wysokosc_raty
# print(tekst.format("lipiec_2", round(pozostalo_kredytu, 2), round(kwota_kredytu - pozostalo_kredytu, 2)), end=" ")
# kwota_kredytu = pozostalo_kredytu
#
# input('wcisnij enter')
# inflacja = Sierpien_2
# pozostalo_kredytu = (1 + ((inflacja + wysokosc_oprocentowania) / 1200)) * kwota_kredytu - wysokosc_raty
# print(tekst.format("sierpień_2", round(pozostalo_kredytu, 2), round(kwota_kredytu - pozostalo_kredytu, 2)), end=" ")
# kwota_kredytu = pozostalo_kredytu
#
# input('wcisnij enter')
# inflacja = Wrzesien_2
# pozostalo_kredytu = (1 + ((inflacja + wysokosc_oprocentowania) / 1200)) * kwota_kredytu - wysokosc_raty
# print(tekst.format("wrzesien_2", round(pozostalo_kredytu, 2), round(kwota_kredytu - pozostalo_kredytu, 2)), end=" ")
# kwota_kredytu = pozostalo_kredytu
#
# input('wcisnij enter')
# inflacja = Pazdziernik_2
# pozostalo_kredytu = (1 + ((inflacja + wysokosc_oprocentowania) / 1200)) * kwota_kredytu - wysokosc_raty
# print(tekst.format("pazdzienik_2", round(pozostalo_kredytu, 2), round(kwota_kredytu - pozostalo_kredytu, 2)), end=" ")
# kwota_kredytu = pozostalo_kredytu
#
# input('wcisnij enter')
# inflacja = Listopad_2
# pozostalo_kredytu = (1 + ((inflacja + wysokosc_oprocentowania) / 1200)) * kwota_kredytu - wysokosc_raty
# print(tekst.format('Listopad_2', round(pozostalo_kredytu, 2), round(kwota_kredytu - pozostalo_kredytu, 2)), end=" ")
# kwota_kredytu = pozostalo_kredytu
#
# input('wcisnij enter')
# inflacja = Grudzien_2
# pozostalo_kredytu = (1 + ((inflacja + wysokosc_oprocentowania) / 1200)) * kwota_kredytu - wysokosc_raty
# print(tekst.format("Grudzien_2", round(pozostalo_kredytu, 2), round(kwota_kredytu - pozostalo_kredytu, 2)), end=" ")
# kwota_kredytu = pozostalo_kredytu
#
#
#
