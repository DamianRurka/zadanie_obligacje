import sys
from MANAGER import manager


identyfikator= (sys.argv[2])
cena_sztuki = (sys.argv[3])
liczba_sztuk = (sys.argv[4])

manager.execute("zakup",identyfikator,int(cena_sztuki),int(liczba_sztuk))
manager.zapis("zakup",identyfikator,cena_sztuki,liczba_sztuk)