print('witaj uzytkowniku')
print('\nTo jest program zawierający \n4 mini programy')
print('\nUruchomić poszczegolny program mozna w nastepujacy sposob:')
print('\nWybierasz: program_obliczeniowy, wpisz : 1')
print('\nWybierasz: obrazek, wpisz: 2')
print('\nWybierasz: zgadnij , wpisz: 3')
print('\nWybierasz: gra o kase , wpisz 4')

program = int(input(""))

if program == 1:
    print('\n\nWITAJ W PROGRAMIE : PROGRAM OBLICZENIOWY')
    print('\nZacznijmy obliczanie :)')
    imie = input("\nJak masz na imie? ")
    print('ponizsze dane wprowadzaj za pomoca cyfr a nie słów')
    dzien = int(input('podaj dzien urodzin: '))
    miesiac = int(input('podaj miesiac twoich urodzin: '))
    rok = int(input('podaj rok urodzenia: '))
    obecny_rok = int(input('podaj aktualny rok: '))
    obecny_m = int(input('podaj aktualny miesiac: '))
    obecny_d = int(input('podaj aktualny dzien'))
    waga = int(input('podaj swoją wagę: '))
    tekst = 'Witaj {} {} masz {} lat '
    print(tekst.format(imie.upper(), '!', obecny_rok - rok))
    print('przepraszam ze na ciebie krzycze :) ')
    print('wybacz')
    bajka = 'łącznie żyjesz {} minut '
    # zmienna grawi to wynik odjecia wagi na ziemii od wagi na jowiszu
    grawi = (waga * 2.528) - waga
    miesiace = obecny_m - miesiac
    dni = obecny_d - dzien
    lata = obecny_rok - rok
    # glowkowanie nad wzorem wyliczenia:
    # (miesiace * 30 * 24 * 60)+(dni * 24 * 60)+(lata * 365 * 24 * 60)
    # (obecny_m - miesiac)
    # (obecny_d - dzien)
    # (obecny_rok - rok)
    tekst_waga = 'na jowiszu ważył byś {} kg'
    print(bajka.format((miesiace * 30 * 24 * 60) + (dni * 24 * 60) + (lata * 365 * 24 * 60)))

    sekundy = '{} sekund'
    # uwazaj gdzie wstawiasz np:  (5+5)×60
    # wynik powyzszego dzialania bedzie wygladal tak 101010101010 .
    #    nie popelniaj bledow ;)
    print('jesli chodzi o sekundy to bedzie to: ')
    print(sekundy.format((miesiace * 30 * 24 * 60) + (dni * 24 * 60) + (lata * 365 * 24 * 60) * 60))
    print(tekst_waga.format(round(waga * 2.528)))
    input('')
    jowisz_t = 'wiec się ciesz że wazysz na ziemi {} kg mniej niz na jowiszu'
    print(jowisz_t.format(round(grawi)))
    dzieki = 'dziekuje ci {} za skorzystanie z mojego programu '
    print(dzieki.format(imie.capitalize()))
    print('\n\nAutorem programu jest : Damian Rurka')
    print('\n\nWersja programu 1.1.0')
    # planowany rozwoj tego programu obliczeniowego
    # -pobor wiekszej ilosci danych
    # stworzenie galezi dalszy_rozwoj
    # -poprawienie nazw zmiennych i wdrozenie zmian poprzez merge  z galezi dalszy_rozwoj na branch master
    # jest to program testowy w ktorym beda implementowane wszystkie kolejne projekty  i wdrazane nowe funkcjonalnosci
elif program == 2:
    print('\n\nWITAJ W PROGRAMIE OBRAZEK')

    print('''

        _____
       |  ___|        □
       |  |__        □□□           _  __   ____
       |  __|         □           | |/ /  / □  |
       |  |   | |_| | □  | |_| |  |   /    \  /_
       |_|    |_____| □  |_____|   |_|      \___|
           ___
         /   _|      
         |  |        ◇    ■                  _  __   ___
         |  |    ●●  ◇    ■   ___    ___    | |/ /  / __|
         |  |__ ●  ● ◇    ■  | ● |  | ● |   |   /   _\ \ 
         \____|  ●●  ◇◇   ■■ |___|l |___|l   |_|   /___/



                 ''')

elif program == 3:
    print("WITAJ W PROGRAMIE ZGADNIJ")
    print('\n\nPodpowiedź: \n\nTeletubisie mówią "..." ')
    haslo = input('podaj odpowiedz: ')
    if haslo == 'papa':
        print("\nTELETUBISIE MÓWIĄ PAPA , \nWiec wcisnij enter by sie z nimi pozegnac")
        input("")
    else:
        print("taka prosta odpowiedz a ty jej nie znasz ")

# program zgadnij przerob na mini milionerzy

elif program == 4:
    print("WITAJ W PROGRAMIE: ")
    print('\n\n\n\t\t"GRA O 10000 : FAKE MONEY" ')
    print('\n\n\n\n\nZaczynamy !')
    print('\nPytanie pierwsze:')
    print('\nJaka mysz chodzi na dwóch nogach?')
    print("A:  Myszka mick'y")
    print("B:  Mysz domowa")
    print("C:  Mysz leśna")
    print("D:  Lama?")
    pierwsza = input('\nPodaj odpowiedz: ')
    if pierwsza == 'A':
        print("gratulacje wygrałeś 1000złoty")
        print("\nPytanie drugie: ")
        print("\nJaka kaczka chodzi na dwóch nogach?")
        print("A:kaczor donald")
        print("B:kaczki latają")
        print("C:kaczki plywaja")
        print("D:kazda ")

        druga = input('\nPodaj odpowiedz: ')
        if druga == 'D':
            print("gratulacje wygrałeś 3000złoty")
            print("\nPytanie trzecie: ")
            print(
                "\nMama Kasi ma pięć córek. Jeśli imiona jej córek'\
                 to odpowiednio Klara, Karolina, Klaudia, Kinga to jakie będzie imię piątej córki?")
            print("\n")
            print("A:Kornelia")
            print("B:Karolina")
            print("C:Kasia")
            print("D:Kinga")
            trzecia = input("\nPodaj odpowiedz: ")
            if trzecia == 'C':
                print("\n\n\n\t\t\tGRATULACJE WYGRAŁEŚ 10000 ZŁOTY")
                input('\n\nWciśnij enter by zakonczyc program')


            else:
                print("Koniec gry , przegrales! ale masz gwarantowane 1000zł")
        else:
            print("Koniec gry , przegrałeś!")
    else:
        print("Koniec gry , przegrałeś!")
else:
    print("Nawet nie zacząłeś  !")