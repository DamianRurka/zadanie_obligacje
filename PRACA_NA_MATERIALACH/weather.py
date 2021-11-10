import requests
import sys
import datetime
import json

link = "https://weatherapi-com.p.rapidapi.com/current.json"
today = datetime.date.today()
#rzykladowa_data_w_slowniku = '2021-11-13'
#Sprawdzenie czy klucz data jest taki sam w 'zapis_pogody.json'
#if str(today) == przykladowa_data_w_slowniku:
#    print("True")


class POGODA:
    def __init__(self,Klucz,data=str(today)):
        self.Klucz = Klucz
        self.data = data
        self.wyslijdane = self.wyslij_dane_pobierajace
        self.czytaj = self.czytanie_slownika()
        self.headers = {
            'x-rapidapi-host': "weatherapi-com.p.rapidapi.com",
            'x-rapidapi-key': Klucz
        }

    def wyslij_dane_pobierajace(self):
        wyslane = {"q": "Malbork,uk", "lat": "0", "lon": "0",
                   "callback": "test", "id": "2172797",
                   "lang": "null", "units": "imperial", "mode": "xml"}
        pobrane = requests.get(link, params=wyslane, headers=self.headers)
        self.req = pobrane.json()
        self.czytanie_slownika()
    def czytanie_slownika(self):
        with open('zapis_pogody.json', 'r') as plik1:
            print(json.load(plik1))
            if self.data == ['localtime'] in json.load(plik1):
                self.status_opadow()
            else:
                self.zapis_slownika()
                self.status_opadow()
            #wczytaj plik i wyszukaj localtime jesli jest odczytaj pogodę
            #w przeciwnym przypadku jeśli plik jest pusty lub nie ma daty uzyj zapis slownika i
            # ponownie sprawdz status opadów

    def zapis_slownika(self):
        with open('zapis_pogody.json', 'a') as plik:
            json.dump(self.req,plik)

    def status_opadow(self):
        with open('zapis_pogody.json', 'r') as plik1:
            opady = json.load(plik1)
            for idx in opady.json()['current']:
                mm = idx[ 'precip_mm']
                if mm == 0.0:
                    print('Nie bedzie padac')
                elif mm > 0.0:
                    print('bedzie padac')
                else:
                    print('nie wiem')

wejscie= POGODA(Klucz = sys.argv[1], data = sys.argv[2])

print(wejscie.wyslij_dane_pobierajace())


# #python weather.py API KEY 2021-11-11