import requests
import sys
import datetime
today = datetime.date.today()
url = "https://weatherapi-com.p.rapidapi.com/current.json"

class Pogoda:
    def __init__(self,Klucz,data=str(today)):
        self.Klucz = Klucz
        self.data = data
        self.dane= self.zapisz_dane_dict()

    def zapisz_dane_dict(self):
        querystring = {'key': self.Klucz, "q": "Malbork,uk", "lat": "0", "lon": "0",
                   "callback": "test", "id": "2172797",
                   "lang": "null", "units": "imperial", "mode": "xml"}
        pobrane = requests.get(url, params=querystring)
        p=pobrane.json()
        return p

apiurl = "weatherapi-com.p.rapidapi.com",
key = "aeb21c175emsh53abf9d14a8c350p1fa3fejsn3b832d50a076"

wejscie= Pogoda(Klucz = sys.argv[1], data = sys.argv[2])
print(wejscie)