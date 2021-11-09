import requests
import sys
import datetime
import json

link = "https://weatherapi-com.p.rapidapi.com/current.json"
today = datetime.date.today()
#rzykladowa_data_w_slowniku = '2021-11-13'
#Sprawdzenie czy klucz data jest taki sam w plik.json
#if str(today) == przykladowa_data_w_slowniku:
#    print("True")


class POGODA:
    def __init__(self,Klucz,data=str(today)):
        self.Klucz = Klucz

        self.data = data
        self.zapiszdane = self.zapisz_dane_dict
        self.slownikdane = self.slownik_danych
        print(self.Klucz)
        self.headers = {
            'x-rapidapi-host': "weatherapi-com.p.rapidapi.com",
            'x-rapidapi-key': Klucz
        }



    def zapisz_dane_dict(self):
        wyslane = {"q": "Malbork,uk", "lat": "0", "lon": "0",
                   "callback": "test", "id": "2172797",
                   "lang": "null", "units": "imperial", "mode": "xml"}
        pobrane = requests.get(link, params=wyslane, headers=self.headers)
        self.req = pobrane.json()
        return self.req

    # czytanie pliku
    # def slownik_danych_read(self):  # read
    #     with open('zapis_pogody.json', 'r') as plik1:
    #         json.load(plik1)

    def slownik_danych(self): #dopisywanie a nie nadpisywanie danych w plik.txt
        with open('zapis_pogody.json', 'w') as plik:
            json.dump(self.req,plik)


    def status_opadow(self):
        opady = "precip_mm" #<-key

        #jesli data byla juz wpisana sprawdz w slowniku dict(plik) czy opady sa równe czy wieksze od 0
        #if opady == 0 print('nie pada)
        #elif opady > 0 print('bedzie padac')
        #else: print("nie wiem")
        #jeßli data jest pierwszy raz wpisana poiteruj po slowniku otrzymanych danych i wypisz wynik operacji
        #lub dodaj dane do pliku.txt i poiteruj po wczytanych danych
        #najlepiej zeby  kazdy otrzymany wynik byl slownikiem a jego kluczem byla by data



wejscie= POGODA(Klucz = sys.argv[1], data = sys.argv[2])
# print(wejscie.text)
#print(wejscie.slownik_danych())
# print(wejscie.json)
print(wejscie.zapisz_dane_dict())
#print(wejscie)
# #python weather.py API KEY 2021-11-11