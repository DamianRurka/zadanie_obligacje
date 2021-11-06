class Magazyn:
    def __init__(self, historia):
        self.stan_magazynowy = {}
        self.historia = historia
        self.stan_konta = 0

    def saldo(self, komenda):
        if self.stan_konta + int(komenda[1]) >= 0:
            self.stan_konta += int(komenda[1])

    def sprzedaz(self, komenda):
        if self.stan_magazynowy.get(komenda[1], 0) >= int(komenda[3]):
            self.stan_konta += int(komenda[2]) * int(komenda[3])
            self.stan_magazynowy[komenda[1]] -= int(komenda[3])

    def zakup(self, komenda):
        if self.stan_konta - int(komenda[2]) * int(komenda[3]) >= 0:
            if self.stan_magazynowy.get(komenda[1], None) is None:
                self.stan_magazynowy[komenda[1]] = int(komenda[3])
            else:
                self.stan_magazynowy[komenda[1]] += int(komenda[3])
            self.stan_konta -= int(komenda[2]) * int(komenda[3])

    def przeglad(self, komenda):
        print(self.historia[int(komenda[1]):int(komenda[2])+1])

    def konto(self):
        print(self.stan_konta)

    def stan_magazynu(self):
        print(self.stan_magazynowy)

    def oblicz_aktualny_stan(self):
        for komenda in self.historia:
            self.wykonaj_komende(komenda)

    def wykonaj_komende(self, komenda):
        if komenda[0] == "saldo":
            self.saldo(komenda)
        if komenda[0] == "sprzedaz":
            self.sprzedaz(komenda)
        if komenda[0] == "zakup":
            self.zakup(komenda)
        if komenda[0] == "konto":
            self.konto()
        if komenda[0] == "magazyn":
            self.stan_magazynu()
        if komenda[0] == "przeglad":
            self.przeglad(komenda)

    def dopisz_historia(self, komenda):
        if komenda[0] in ["saldo", "sprzedaz", "zakup"]:
            self.historia.append(komenda)
