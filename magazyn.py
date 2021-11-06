class Magazyn:
    def __init__(self, history):
        self.history = history
        self.stan_magazynowy = {}
        self.stan_konta = 0

    def saldo(self, komenda):
        if self.stan_konta + komenda[1] >= 0:
            self.stan_konta += komenda[1]

    def sprzedaz(self, komenda):
        if self.stan_magazynowy.get(komenda[1], 0) >= komenda[3]:
            self.stan_konta += komenda[2] * komenda[3]
            self.stan_magazynowy[komenda[1]] -= komenda[3]

    def zakup(self, komenda):
        if self.stan_konta - komenda[2] * komenda[3] >= 0:
            if self.stan_magazynowy.get(komenda[1], None) is None:
                self.stan_magazynowy[komenda[1]] = komenda[3]
            else:
                self.stan_magazynowy[komenda[1]] += komenda[3]
            self.stan_konta -= komenda[2] * komenda[3]


    def oblicz_aktualny_stan(self):
        for komenda in self.history:
            if komenda[0] == 'saldo':
                self.saldo(komenda)
            if komenda[0] == 'sprzedaz':
                self.sprzedaz(komenda)
            if komenda[0] == 'zakup':
                self.zakup(komenda)


    def konto(self,):
        print(self.stan_konta)
    #def przegląd(self, komenda):
 # print(self.historia[int(komenda[1]):int(komenda)[2]) + 1])