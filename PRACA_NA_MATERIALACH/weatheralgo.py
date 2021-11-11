import requests
import sys
import datetime
import json
import pprint
link = "https://weatherapi-com.p.rapidapi.com/current.json"
today = datetime.date.today()

class POGODA:
    def __init__(self,Klucz,data=str(today)):
        self.Klucz = Klucz
        self.data = data
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
        self.opady = self.req['current']['precip_mm']
        self.data_z_api = self.req['location']['localtime'].split(' ')[0]
        self.pustyslownik()
        self.sprawdzanie_daty_w_slowniku()

    def pustyslownik(self):
        self.slownik_data_opady = {}

    def sprawdzanie_daty_w_slowniku(self):
        if self.data in self.slownik_data_opady[self.data_z_api] and self.data == self.slownik_data_opady[self.data_z_api]:
            self.odczyt_pogody_format()
            self.zapis_slownika_w_pliku()
            self.status_opadow()
        else:
            self.dodawanie_do_slownika()
            self.odczyt_pogody_format()
            self.zapis_slownika_w_pliku()
            self.status_opadow()

    def dodawanie_do_slownika(self):
        self.slownik_data_opady = {self.data_z_api: self.opady}


    def zapis_slownika_w_pliku(self):
        with open('zapis_pogody.json', 'w') as plik:
            json.dump(self.slownik_data_opady, plik)

    def odczyt_pogody_format(self):
        self.format = {self.data1 : self.status_opadow()}
        with open('odczyt_pogody.json', 'w') as plik:
            json.dump(self.format, plik)
        with open('odczyt_pogody.json', 'r') as plik:
            print(json.load(plik))

    def status_opadow(self):
        with open('zapis_pogody.json', 'r') as plik1:
            json.load(plik1)

            if self.slownik_data_opady['<co tu wpisac>'] == 0.0:
                print('Nie bedzie padac')
            elif self.slownik_data_opady['<co tu wpisac>'] > 0.0:
                print('bedzie padac')
            else:
                print('nie wiem')


wejscie= POGODA(Klucz = sys.argv[1], data = sys.argv[2])
print(wejscie.wyslij_dane_pobierajace())

#terminal: python weatheralgo.py "aeb21c175emsh53abf9d14a8c350p1fa3fejsn3b832d50a076" 2021-11-10
