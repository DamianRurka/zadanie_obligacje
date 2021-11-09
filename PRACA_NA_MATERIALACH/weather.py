import requests
import sys
import datetime

link = "https://weatherapi-com.p.rapidapi.com/current.json"
today = datetime.date.today()

class POGODA:
    def __init__(self,Klucz,data=str(today)):
        self.Klucz = Klucz
        self.data = data

    def zapisz_dane_dict(self,copyjsonn):
        wyslane = {'key': self.Klucz, "q": "Malbork,uk", "lat": "0", "lon": "0",
                   "callback": "test", "id": "2172797",
                   "lang": "null", "units": "imperial", "mode": "xml"}
        pobrane = requests.get(link, params=wyslane)
        jsonn = pobrane.json()
        self.copyjsonn = jsonn
        return jsonn

    def slownik_danych(self):
        with open('listadanych.txt', 'a') as plik:
            plik.write(self.copyjsonn.text)
            dict(plik)

authorized = POGODA(Klucz = sys.argv[1], data = sys.argv[2])
print(authorized)

#python weather.py API KEY 2021-11-11