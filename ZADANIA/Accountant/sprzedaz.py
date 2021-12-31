import sys
from MANAGER import manager


file_path = sys.argv[1]
identyfikator = (sys.argv[2])
cena_sztuki = (sys.argv[3])
liczba_sztuk = (sys.argv[4])

manager.execute("sprzedaz", identyfikator, int(cena_sztuki), int(liczba_sztuk))
manager.zapis("sprzedaz", identyfikator, cena_sztuki, liczba_sztuk)