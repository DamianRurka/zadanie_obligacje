# from lekcja_import import POWITANIE
# from lekcja_import import print_hello
# from lekcja_import import Point
#
# print(POWITANIE.format())
# p1 = Point(3, 4)
# p2 = Point(5, 12)
# print_hello("ewa")
# print(p1.length() + p2.length())


from lekcja_import import *
# fd = open(filepath, "w") #w przypadku gdy nadpisujemy całą zawartość pliku
# fd = open(filepath, "a") #w przypadku gdy chcemy dopisać nową zawartość do końca pliku

# do pliku dopisujemy zawartość poprzez metody:
#
# fd.write(content) # dopisuje
# fd.write(lines) #dopisuje linie do pliku

#  zamknięcie pliku dzięki instrukcji with:
#
# with open(filepath) as fd:
# 	for line in fd:
# 	print(line)
# print("tego dnia <data> <rodzaj tekstu zalezny od pogody>")

# Czytanie z pliku:
#
# Python pozwala na bezpośrednie edytowanie plików tekstowych za pomocą wbudowanej funkcji open():
# Aby zacząć czytać plik najpierw tworzymy deskryptor pliku:
# fd = open(filepath)
# Podana ścieżka może być stałą, jak również zmienną lub wyrażeniem.
# Z otwartego w ten sposób pliku możemy czytać za pomocą (między innymi) następujących metod:
#
# fd.read() # czyta całość pliku, zwraca go jako str
# fd.read(max_bytes)  # czyta całość pliku, zwraca go jako str maksymalnie max_bytes znaków
# fd.readline()  # czyta jedną linię z pliku
# fd.readline(max_bytes)  # czyta jedną linię z pliku ale nie więcej niż max_bytes
# fd.readlines() #czyta całość pliku, zwraca zawartość pliku w postaci listy ciągów znaków
# (każda linia jako osobny element)
# fd.readlines(max_bytes) #czyta całość pliku, zwraca zawartość pliku w postaci listy ciągów znaków