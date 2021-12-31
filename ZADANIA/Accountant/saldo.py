import sys
from MANAGER import manager


wartosc= (sys.argv[2])
komentarz = sys.argv[3]    #np. Zaliczka od partnerów/zleceniodawców

manager.execute("saldo", int(wartosc), komentarz)
manager.zapis("saldo", wartosc, komentarz)

