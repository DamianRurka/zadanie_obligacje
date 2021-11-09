#Analiza Venv, i pip, skrótowe operacje na dict - warsztaty
import requests
import sys
import datetime

#python weather.py keyapi data
today = datetime.date.today()
print(today)
dane_upload = {"q":"London,uk","lat":"0","lon":"0","callback":"test","id":"2172797","lang":"null","units":"imperial","mode":"xml"}
API_KEY = sys.argv[0]
data = sys.argv[1]
zapisane_dane = ('zapisane_wyniki.txt')
nadpisywanie = open(zapisane_dane, 'w')
czytanie = open(zapisane_dane, 'r')
host = {'x-rapidapi-host': "weatherapi-com.p.rapidapi.com",}
url = "https://weatherapi-com.p.rapidapi.com/current.json"
KEYY ='x-rapidapi-key'+str(API_KEY)
response = requests.request("GET", url, headers=host+KEYY, params=dane_upload)
print(response.text)



#Wczytywanie lini z txt
def loadtxt():
    with open(zapisane_dane, 'r') as plik:
        wczytywanielini = plik.readline().strip()
        if wczytywanielini == False:
            nadpisywanie.write(data + response.text)
            print(czytanie)
        elif data == False:
            print()
            #jesli data nie jest podana w terminalu wykonaj program dla nastepnego dnia



# with open('wyjscie.txt', 'r') as plik:
#     odczyt = plik.readlines()
# print(odczyt)


