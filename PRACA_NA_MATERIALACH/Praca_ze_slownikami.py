import datetime
today = datetime.date.today()
dane_w_slowniku = []
slownik={today:'nie pada'}
dane_w_slowniku.append({today: 'nie pada'})
dane_w_slowniku.append({today: 'nie pada'})     # dodawanie slownika do listy slowników


#print(slownik[today])   #wyswietlenie warości klucza


slownik[(today)] = "nie pada 2"   # dodawanie klucza i jego wartości do slownika !!!!!!!!!!NADPISYWANIE SLOWNIKA
                                  # JESLI TAKI KLUCZ JUZ ISTNIAŁ

for daty in slownik:     #wyswietla klucze w slowniku
        print('klucze w slowniku',daty)
slownik[('2021-12-30')] = "nie wiem"
for data, stan_pogody in slownik.items(): #wyswietla klucze i ich wartości
        print('klucze i wartości w slowniku',data , stan_pogody)
print('dane w slowniku:',dane_w_slowniku)

