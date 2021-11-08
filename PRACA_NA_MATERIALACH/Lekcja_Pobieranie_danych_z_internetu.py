import requests
# TODO:POBIERANIE DANYCH Z WWW
# url = 'https://futurecollars.com/pl/business-intelligence-kurs-online/'
# resp = requests.get(url).text
#
# start_elem = '<h3 class="mentor-name">'
# start_pointer = resp.find(start_elem, 0) # </h3>
# end_elem = '</h3>'
# end_pointer = resp.find(end_elem,start_pointer+len(start_elem))
# print(resp[start_pointer+len(start_elem):end_pointer])


#TODO:COS CO SIE PRZYDA
from pprint import pprint
url = 'https://randomuser.me/api/?gender=female'
resp = requests.get(url)
#pprint(resp.json())
pprint(resp.json()['results'][0]['gender'])
pprint(resp.json()['results'][0]['email'])
pprint(resp.json()['results'][0]['id'])
pprint(resp.json()['info'][0]['version'])
pprint(resp.json()['location'][0]['state'])
pprint(resp.json()['location'][0]['country'])
