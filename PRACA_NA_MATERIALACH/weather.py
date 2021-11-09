import requests
import sys
import datetime
przykladowa_data_w_slowniku = '2021-11-13'
link = "https://weatherapi-com.p.rapidapi.com/current.json"
today = datetime.date.today()
# jak porównać czy wpisana data jest taka sama jak daty znajdujace się w plik.txt
class POGODA:
    def __init__(self,Klucz,data=str(today)):
        self.Klucz = Klucz
        self.data = data
        self.zapiszdane = self.zapisz_dane_dict
        self.slownikdane = self.slownik_danych



    def zapisz_dane_dict(self):
        wyslane = {'key': self.Klucz, "q": "Malbork,uk", "lat": "0", "lon": "0",
                   "callback": "test", "id": "2172797",
                   "lang": "null", "units": "imperial", "mode": "xml"}
        pobrane = requests.get(link, params=wyslane)
        self.req = pobrane.json()
        return self.req

    def slownik_danych(self): #dopisywanie a nie nadpisywanie danych w plik.txt
        with open('zapis_pogody.txt', 'a') as plik:
            plik.write(self.req.text)
            dict(plik)
            return self.zapisz_dane_dict


    def status_opadow(self):
        opady = "precip_mm" #<-key
        opady = pass

        #jesli data byla juz wpisana sprawdz w slowniku dict(plik) czy opady sa równe czy wieksze od 0
        #if opady == 0 print('nie pada)
        #elif opady > 0 print('bedzie padac')
        #else: print("nie wiem")
        #jeßli data jest pierwszy raz wpisana poiteruj po slowniku otrzymanych danych i wypisz wynik operacji
        #lub dodaj dane do pliku.txt i poiteruj po wczytanych danych
        #najlepiej zeby  kazdy otrzymany wynik byl slownikiem a jego kluczem byla by data



wejscie= POGODA(Klucz = sys.argv[1], data = sys.argv[2])
# print(wejscie.text)
# print(wejscie.slownik_danych())
#print(wejscie.json)
print(wejscie)
# print(wejscie.zapisz_dane_dict())

# #python weather.py API KEY 2021-11-11