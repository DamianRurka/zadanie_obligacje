import requests
import sys
import datetime
import json

link = "https://weatherapi-com.p.rapidapi.com/current.json"
today = datetime.date.today()


class POGODA:
    def __init__(self, Klucz, data):
        self.Klucz = Klucz
        self.data = str(data)
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
        self.format_opadow()
        self.data_z_api = self.req['location']['localtime'].split(' ')[0]
        self.data_z_api = str(self.data_z_api)
        self.pustyslownik()
        self.wczytanie_slownika_z_pliku()

    def pustyslownik(self):
        self.slownik_data_opady = []

    def sprawdzanie_daty_w_slowniku(self):          #  <-----  TU PROGRAM SIE BUGUJE
        for daty in self.slownik_data_opady:
            klucze = daty
            if self.data in klucze:
                print(self.slownik_data_opady)

            elif self.data == str(today):
                self.dodawanie_do_slownika()
                self.zapis_slownika_w_pliku()
                self.wczytanie_slownika_z_pliku()
            else:
                print('nie wiem')

    def wczytanie_slownika_z_pliku(self):
        with open('zapis_pogody.json', 'r') as plik:
            self.slownik_data_opady = json.load(plik)
            self.sprawdzanie_daty_w_slowniku()

    def format_opadow(self):
        if self.opady == 0.0:
            self.opady = 'Nie bedzie padac'
        else:
            self.opady = 'bedzie padac'

    def dodawanie_do_slownika(self):
        self.slownik_data_opady[self.data_z_api] = self.opady

    def zapis_slownika_w_pliku(self):
        with open('zapis_pogody.json', 'w') as plik:
            json.dump(self.slownik_data_opady, plik)

wejscie = POGODA(Klucz = sys.argv[1], data = sys.argv[2])
print(wejscie.wyslij_dane_pobierajace())

#terminal: python weatheralgo.py "aeb21c175emsh53abf9d14a8c350p1fa3fejsn3b832d50a076" 2021-11-10


