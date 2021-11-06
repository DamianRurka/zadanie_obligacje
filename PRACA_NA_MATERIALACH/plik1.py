import os

FOLDER = 'pliki'
PLIK_WEJSCIOWY = 'in.txt'

file_path = os.path.join(FOLDER, PLIK_WEJSCIOWY)

def read_history(file_path):
    with open(file_path, 'r') as file:
        for line in file:
            line = line.rstrip()
            if line == 'stop':
                break
            komenda = [line]
            if line == 'saldo':
                value = file.readline().rstrip()
                comment = file.readline().rstrip()
            if line == ['zakup', 'sprzedaz']:
                product_name = file.readline().rstrip()
                product_price = file.readline().rstrip()
                product_value = file.readline().rstrip()
                komenda.extend([product_name , product_price, product_value])
            history.append(komenda)

history = read_history()

file_path = os.path.join(FOLDER, PLIK_WEJSCIOWY)
print('Folder path: "{}" '.format(file_path))
history = []
