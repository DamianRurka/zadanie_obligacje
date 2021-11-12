
# imie = ["Adam", "Ewa", "Marcin", "Krzysztof", "Jakub", "Anita"]
# print(imie[0])

# imie = ["Adam", "Ewa", "Marcin", "Krzysztof", "Jakub", "Anita"]
# startname_index = 0
# print(imie[startname_index]) #adam jest 0
# print(imie[startname_index+1]) #ewa jest 1
# print(imie[startname_index+2]) # marcin jest 2


# firstnames = ["Adam", "Ewa", "Marcin", "Krzysztof", "Jakub", "Anita"]
# print(firstnames[-1])
# #prints Anita
# print(firstnames[1:4])  # 1:4 drukuje imie 1,2,3 , wartość liczby 4 jest nieuwzgledniana
# #prints Jakub
# firstnames = ["Adam", "Ewa", "Marcin", "Krzysztof", "Jakub", "Anita", "marta"]
# len wypisuje liczbę wartości w liście
# list(range(6))
#prints [0, 1, 2, 3, 4, 5]
# for index in range(6):
# 	print(index)

# firstnames = ["Adam", "Ewa", "Marcin", "Krzysztof", "Jakub", "Anita"]
# for firstname in firstnames:
#   print("Imię: {}".format(firstname))              #drukuje liste z wynikami : imie:Adam itd...
#
# firstnames = ["Adam", "Ewa", "Marcin", "Krzysztof", "Jakub", "Anita"]
# print("Dwa ostatnie elementy: {} {}".format(firstnames[-2], firstnames[-1]))   #zamiana wartości
# firstnames.append("Iwona",)
# firstnames.append("marta",)
# print("Dwa ostatnie elementy: {} {}".format(firstnames[-2], firstnames[-1]))

# firstnames = ["Adam", "Ewa", "Marcin", "Krzysztof", "Jakub", "Anita"]
# print("Imię pod indeksem 1 to {}", firstnames[1])                         # zmiana wartości
# firstnames[1] = "Marta"
# print("Imię pod indeksem 1 to {}", firstnames[1])

# firstnames = ["Adam", "Ewa", "Marcin", "Krzysztof", "Jakub", "Anita"]    #dodanie wartości do listy
#                                                                          # w dowolnym miejscu
# for firstname in firstnames:
#   print(firstname)
# firstnames.insert(0, "Marta")
# for firstname in firstnames:
#   print(firstname)
# firstnames_male = ["Adam", "Marcin", "Krzysztof", "Jakub"]
# firstnames_female = ["Ewa", "Anita"]
#
#
# firstnames =  firstnames_male + firstnames_female    # dodawanie listy do listy
# for firstname in firstnames:
#   print(firstname)
# firstnames = ["Adam", "Ewa", "Marcin", "Krzysztof", "Jakub", "Anita"]
# del firstnames[2]                                                          #usunięcie wybranej wartości
# for firstname in firstnames:
#   print(firstname)

# firstnames = ["Adam", "Ewa", "Marcin", "Krzysztof", "Jakub", "Anita"]
# firstnames.remove("Marcin")                                      #usuniecie wartości w wybranej liście
# for firstname in firstnames:
#   print(firstname)

# firstnames = ["Adam", "Ewa", "Marcin", "Krzysztof", "Jakub", "Anita", "Marcin"] # zwróć uwagę na powtórzenie "Marcin"
# print(firstnames.index("Marcin"))       #podaje miejsce znajdowania się podanej wartości w liście (marcin jest 2)

# firstnames = ["Adam", "Ewa", "Marcin", "Marcin" "Krzysztof", "Jakub", "Anita", "Marcin", "Marcin"] # zwróć uwagę na powtórzenie "Marcin"
# print(firstnames.index("Marcin"))
# print(firstnames.index("Marcin", 4))
# #TODO: coś tu nie działa



#poniżej sprawdzenie czy element znajduje się w liście + dodanie elementu i wyswietlenie
#komunikatu że podane imie jest dostępne

# firstnames = ["Adam", "Ewa", "Marcin", "Krzysztof", "Jakub", "Anita"]
# if "Jakub" in firstnames:
#   print("Imię Jakub jest dostępne")
# else:
#   print("Ten blok nie będzie wykonany")
# firstnames.insert(1, input("imie"))
# if "Weronika" in firstnames:
#     print("Imię Weronika jest dostępne")

#true i false (jeśli sie coś znajduje w liście lub nie
#samplelist-nazwa listy i czy coś się w niej znajduje

# sample_list = []
# print(bool(sample_list)) # returns False
# sample_list = ["a", "b"]
# print(bool(sample_list)) # returns True
# sample_list = [""]
# print(bool(sample_list)) # returns True


# w liśie się coś znajduje lub nie

# sample_list = ["twój stary pijany"]
# if sample_list:
# 	print("Lista ma elementy")
# else:
# 	print("Lista jest pusta")
#
# sample_list = []
# if sample_list:
# 	print("Lista ma elementy")
# else:
# 	print("Lista jest pusta")
      #TODO : tuple  tuple-niemodyfikowalna lista!!!!!!!!!!!!
# empty_tuple = tuple([])
# integer_tuple = 1, 2, 3, 4
# mixed_tuple = "a", 1, "b", 2, True
# single_element_tuple = tuple(["single element"])
# single_element_tuple = "single element", # przecinek na końcu!
# tuple_inside_of_list = [(1, 2), (3,), 4, 5]
# mixed_tuple = "a", 1, "b", 2, True
# print(mixed_tuple[4])


# Metoda .index, jak i operatory "in", "not in" również są dostępne.

mixed_tuple = "a", 1, "b", 2, True
print(mixed_tuple.index("b"))
print("a" in mixed_tuple)#wynikiem tego "printa" będzie true bo a jest w liście
# ( jeśli chcemy wydrukować "a" to musimy podać numer elementu w liście czyli 0
print(mixed_tuple [0])

# Tuple mogą być przekształcane w listy, a listy w tuple.
 # TODO: zmiana tupla na liste i na odwrót
# mixed_tuple = "a", 1, "b", 2, True
# mixed_list = list(mixed_tuple)
#
# mixed_list2 = ["a", 1, "b", 2, True]
# mixed_tuple2 = tuple(mixed_list2)


# a, b = 1, 2
# print(a) #=2
# print(b) #=1

# t1 = 1, 2     #obowiązuje kolejność a=1 b=2
# a, b = t1
#
# print(b)

#
# #Dla dwóch indeksów firstname i lastname wypisz wartości w jednej lini
# # a i b to firstname i lastname
# fullnames = [
# 	("Adam", "Abacki"),
# 	("Bartosz", "Babacki"),
# 	("Czesław", "Cabacki")
# ]
# for a, b in fullnames:
# 	print("{} {}".format(a, b))


#  #TODO enumerate imie1:adam itd
# firstnames = ["Adam", "Ewa", "Marcin", "Krzysztof", "Jakub", "Anita"]
# for index, firstname in enumerate(firstnames):
#   print("Imię {}: {}".format(index+1, firstname))

 #TODO id zmiennej itp:
# a = 1
# print(id(a))
# a = a+1
# print(id(a))

# sample_set = {"a", "b", "c", 1, True}
# print("a" in sample_set)
# print("d" not in sample_set)

#Wartości są unikalne, to znaczy wielokrotne dodanie tej samej wartości nie zwiększa rozmiaru zbioru:
#
# sample_set = {"a", "b", "c"}
# sample_list = ["a", "b", "c"]
# print("set:{} list: {}".format(len(sample_set), len(sample_list)))
# sample_set.add("c")
# sample_list.append("c")
# print("set:{} list: {}".format(len(sample_set), len(sample_list)))

#wynik:
# # set:3 list: 3
# # set:3 list: 4


# sample_dict = "a": 1, "b": 2, "c"
# for k, v in sample_dict.items():
#   print("{}: {}".format(k, v)                  TODO:tu też coś nie działa

#