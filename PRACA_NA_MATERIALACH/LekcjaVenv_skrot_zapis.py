# imie = "Adam"
# if imie[-1] == "a":
# 	plec1 = "kobieta"
# else:
# 	plec1 = "mezczyzna"
# print(plec1)
# #Skrót
# imie = "kasia"
# plec2 = "kobieta" if imie[-1] == "a" else "mezczyzna"
# print(plec2)
#
#
# a = ["adam", "Ewa", "wojtek", "Robert", "marcin", "michał"]
# lista2 = []
# for imie in a:
# 	lista2.append(imie.capitalize())
# print(a)
# print(lista2)


#lst_a = ["adam", "Ewa", "wojtek", "Robert", "marcin", "michał"]
#lst_b = [imie2.capitalize() for imie2 in lst_a]

#Powyższy zapis pozwala również na filtrowanie elementów starej listy. Rozważmy następujący kod:
#
# lst_a = ["adam", "Ewa", "wojtek", "Robert", "marcin", "michał"]
# lst_b = []
# for firstname in lst_a:
# 	if firstname != firstname.capitalize():
# 		lst_b.append(firstname.capitalize())
# print(lst_b)

#wynik ['Adam', 'Wojtek', 'Marcin', 'Michał']

#skrót
# #
lst_a = ["adam", "Ewa", "wojtek", "Robert", "marcin", "michał"]
# lst_b = [firstname.capitalize() for firstname in lst_a if firstname != firstname.capitalize()]
# print(lst_a)
# print(lst_b)
# set_a = {firstname.capitalize() for firstname in lst_a if firstname != firstname.capitalize()}
# print(set_a)
# dict_a = {firstname: firstname.capitalize() for firstname in lst_a}
# print(dict_a)


liczby	= [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
lista_laczna = [liczba for malalista in liczby for liczba in malalista]
print(lista_laczna)
print(liczby)
print([sum(lista_laczna)])
print([sum(a) for a in liczby]) #sumowanie liczb w listach wewnetrznych

#Rozbijanie słów na poszczególne litery w liście
rozbite = [list(a) for a in lst_a]
print(rozbite)
#TODO: LACZENIE LIST W NP: SLOWNIK key polska value:warszawa
panstwa = ['Polska' , 'Niemcy' , 'Rosja', 'USA' ]
stolice = ['warszawa','berlin','moskwa','washington']

slownik_P_S = dict(zip(panstwa,stolice))
print(slownik_P_S)

nieunia = ['Rosja', 'Wielka_Brytania']
unia = {panstwo: stolica for panstwo, stolica in slownik_P_S.items() if panstwo not in nieunia}
print(unia)
#TODO:UWAZAJ NA SPACJE I INNE ZNAKI NP "GAPA " "GAPA"  dla komputera to nie jest to samo

lista_tupli = [(1,2),(3,4),(5,6)]
print(dict(lista_tupli))
#TODO:Stworzenie słownika z listy tupli






#TODO:PIP
#pip freeze > requirements.txt  #zapis zainstalowanych pakietów do pliku
#pip install -r requirements.txt #Instalacja pakietów podanych w pliku
#python -m pip install --upgrade pip #aktualizacja pip
