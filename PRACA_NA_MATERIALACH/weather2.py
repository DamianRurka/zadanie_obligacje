import pprint
import requests
import sys
import datetime

link = "https://weatherapi-com.p.rapidapi.com/current.json"
today = datetime.date.today()

class POGODA:
    def __init__(self,Klucz,data=str(today)):
        self.Klucz = Klucz
        self.data = data
        self.dane = self.zapisz_dane_dict


    def zapisz_dane_dict(self,):
        wyslane = {'key': self.Klucz, "q": "Malbork,uk", "lat": "0", "lon": "0",
                   "callback": "test", "id": "2172797",
                   "lang": "null", "units": "imperial", "mode": "xml"}
        pobrane = requests.get(link, params=wyslane)
        req = pobrane.json()
        return req

wejscie= POGODA(Klucz = sys.argv[1], data = sys.argv[2])
pprint.pprint(wejscie)

