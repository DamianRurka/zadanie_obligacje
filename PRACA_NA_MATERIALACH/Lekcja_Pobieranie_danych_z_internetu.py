import requests

url = 'https://futurecollars.com/pl/business-intelligence-kurs-online/'
resp = requests.get(url).text

start_elem = '<h3 class="mentor-name">'
start_pointer = resp.find(start_elem,0) #</h3>
end_elem = '<\h3>'
end_pointer = resp.find(end_elem,start_pointer+len(start_elem))
print(resp[start_pointer+len(start_elem):end_pointer])

