import requests
import sys
url = "https://weatherapi-com.p.rapidapi.com/current.json"

querystring = { "q": "Malbork,uk", "lat": "0", "lon": "0",
                   "callback": "test", "id": "2172797",
                   "lang": "null", "units": "imperial", "mode": "xml"}


headers = {
    'x-rapidapi-host': "weatherapi-com.p.rapidapi.com",
    'x-rapidapi-key': "aeb21c175emsh53abf9d14a8c350p1fa3fejsn3b832d50a076"
    }

# headers = {
#     'x-rapidapi-host': "weatherapi-com.p.rapidapi.com",'{}'.format(a)}
# headers[1] = sys.argv[1]
# a = headers[1]

response = requests.request("GET", url, headers=headers, params=querystring)

print(response.text)