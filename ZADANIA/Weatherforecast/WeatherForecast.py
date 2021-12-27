import os
import requests
import sys
import datetime
import json
separator=("-"*30)
link = "https://weatherapi-com.p.rapidapi.com/current.json"
today = datetime.date.today()


class WeatherForecast:
    def __init__(self, Klucz, data):
        self.Klucz = Klucz
        self.data = str(data)
        self.headers = {
            'x-rapidapi-host': "weatherapi-com.p.rapidapi.com",
            'x-rapidapi-key': Klucz
        }

    def __getitem__(self, data):
        wyslane = {"q": "Malbork,uk", "lat": "0", "lon": "0",
                   "callback": "test", "id": "2172797",
                   "lang": "null", "units": "imperial", "mode": "xml"}
        pobrane = requests.get(link, params=wyslane, headers=self.headers)
        self.req = pobrane.json()
        self.opady = self.req['current']['precip_mm']
        self.data_z_api = self.req['location']['localtime'].split(' ')[0]
        self.data_z_api = str(self.data_z_api)
        self.pustyslownik()
        self.wczytanie_slownika_z_pliku()
        self.format_opadow()
        return self.slownik_data_opady.get(data,"-----------------------------------------------------")


    def pustyslownik(self):
        self.slownik_data_opady = {}

    def sprawdzanie_daty_w_slowniku(self):  # <-----  TU PROGRAM SIE BUGUJE
        if self.data in self.slownik_data_opady.keys():
            print(self.slownik_data_opady[self.data])
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

    def items(self):
        for key,element in self.slownik_data_opady.items():
            element =  "bedzie padac" if float(element) > 0.0 else "nie będzie padać"
            yield tuple([key , element])

    def __iter__(self):
        return iter(self.slownik_data_opady.keys())


wf = WeatherForecast(Klucz=sys.argv[1], data=sys.argv[2])

print(wf["data"])

for idx in wf.items():
    print(idx)
print(separator)
for daty in wf:
    print(daty)
# terminal: python WeatherForecast.py "aeb21c175emsh53abf9d14a8c350p1fa3fejsn3b832d50a076" 2021-12-21