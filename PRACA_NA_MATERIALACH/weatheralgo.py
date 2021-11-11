import requests
import sys
import datetime
import json

link = "https://weatherapi-com.p.rapidapi.com/current.json"
today = datetime.date.today()


class POGODA:
    def __init__(self, Klucz, data=str(today)):
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
        if self.opady == 0.0:
            self.opady = 'Nie będzie padać'
        else:
            self.opady = 'będzie padać'


        self.data_z_api = self.req['location']['localtime'].split(' ')[0]
        self.pustyslownik()
        self.sprawdzanie_daty_w_slowniku()

    def pustyslownik(self):
        self.slownik_data_opady = []

    def sprawdzanie_daty_w_slowniku(self):
        for daty in self.slownik_data_opady:

            if self.data in self.slownik_data_opady:
                self.odczyt_pogody_format()
                self.zapis_slownika_w_pliku()
                self.status_opadow()
            else:
                self.dodawanie_do_slownika()
                self.odczyt_pogody_format()
                self.zapis_slownika_w_pliku()
                self.status_opadow()

    def dodawanie_do_slownika(self):
        self.slownik_data_opady[self.data_z_api] = self.opady


    def zapis_slownika_w_pliku(self):
        with open('zapis_pogody.json', 'w') as plik:
            json.dump(self.slownik_data_opady, plik)

    def odczyt_pogody_format(self):
        self.format = {self.data_z_api : self.status_opadow()}
        with open('odczyt_pogody.json', 'w') as plik:
            json.dump(self.format, plik)
        with open('odczyt_pogody.json', 'r') as plik:
            print(json.load(plik))

    def status_opadow(self):
        with open('zapis_pogody.json', 'r') as plik:
            json.load(plik)

            if self.slownik_data_opady[self.data_z_api] == 0.0:
                print('Nie bedzie padac')
            elif self.slownik_data_opady[self.data_z_api] > 0.0:
                print('bedzie padac')
            else:
                print('nie wiem')


    #def slownik_docelowy(self): # ten slownik będzie przyjmował jako klucz date a
    # wartość jako wynik funkcji status opadów i odnosił się do funkcji zapis slownika w pliku
    # obecna funkcja zapis slownika do pliku bedzie musiala byc edytowana pod nazwe nowego slownika
    # dodaj funkcje która wyswietli dane z pliku gdy podana data sys.argv w terminalu będzie znajdowała się
    # w słowniku, wypisz nie wiem jesli podana data z przeszlosci w sys argv nie znajdowala się w pliku.json lub
    # data jest z przyszłości



wejscie = POGODA(Klucz = sys.argv[1], data = sys.argv[2])
print(wejscie.wyslij_dane_pobierajace())

#terminal: python weatheralgo.py "aeb21c175emsh53abf9d14a8c350p1fa3fejsn3b832d50a076" 2021-11-10


