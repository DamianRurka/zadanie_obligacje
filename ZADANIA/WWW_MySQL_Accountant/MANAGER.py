import sys
import json

class CzytnikPliku:

    def __init__(self, file_path):
        self.file_path = file_path
        self.historia = []


    def read_lines(self):

        with open(self.file_path, "r") as plik:
            for line in plik:
                line = line.strip()
                if line == "stop":
                    break
                try:
                    line = float(line)
                except ValueError:
                    pass
                self.historia.append(line)

    def save_lines(self, nowe_dane):
        with open(self.file_path, "w") as plik:
            plik.writelines([str(line) +'\n' for line in nowe_dane])

    def __print(self):
        print(self.historia)


class Manager:
    def __init__(self, CzytnikPliku):
        self.actions = {}
        self.account = 0
        self.storage = {}
        self.historia = CzytnikPliku.historia
        self.zapis_wykonanych_akcji = []


    def assign(self, name):

        def decorate(func):
            self.actions[name] = func
        return decorate


    def execute(self, name, *args, **kwargs):

        if name not in self.actions:
            raise Exception
        self.actions[name](self, *args, **kwargs)

    def zapis(self, *args):

        with open("in.txt", "w") as plik:

            for komenda in self.historia:
                for akcja in komenda:
                    plik.write(str(akcja)+ "\n")
            if args:
                plik.writelines([element + '\n' for element in args])
            plik.write("stop")


    def magazynier(self, nazwa_produktu, value, quantity):
        if quantity < 0:
            if nazwa_produktu in self.storage:
                if (self.storage.get(nazwa_produktu) + quantity) >= 0:
                    self.storage[nazwa_produktu] = self.storage.get(nazwa_produktu) + quantity
                else:
                    print("Brak wystarczajacej ilosci sztuk {}  w magazynie".format(nazwa_produktu))
                    return False
            else:
                print("Brak takiego produktu")
                return False
        else:
            if nazwa_produktu in self.storage:
                self.storage[nazwa_produktu] = self.storage.get(nazwa_produktu) + quantity
            else:
                self.storage[nazwa_produktu] = quantity


    def zapis_akcji(self, action, parameters):
        self.zapis_wykonanych_akcji.append({'action': action, "parameters": tuple(parameters)})


    def data_loader(self):

        historia = []
        komenda = []

        for akcja in self.historia:
            if akcja in ["saldo", "zakup", "sprzedaz"]:
                if komenda:
                    self.execute(komenda[0], *komenda[1:])
                    historia.append(komenda)
                komenda = []
            komenda.append(akcja)
        historia.append(komenda)
        self.historia = historia



fh = CzytnikPliku("in.txt")
fh.read_lines()

manager = Manager(fh)

@manager.assign("przeglad")
def przeglad(manager, start, end, *args, **kwargs):
    sl = print(manager.historia[start:end + 1])
    path = "przeglad.txt"
    with open(path, 'w') as f:
        f.write(str(sl))


@manager.assign("magazyn")
def magazyn(manager, identifier, *args, **kwargs):
    sl = ()
    for produkt in identifier:
        if produkt in manager.storage:
            stan = manager.storage.get(produkt)
        else:
            stan = 0
        sl += ( produkt ,stan )
        path = "magazyn.txt"
        with open(path, 'w') as f:
            f.write(str(sl))


@manager.assign("zakup")
def zakup(manager, identifier, value, quantity,  *args, **kwargs):
    if value > 0 and quantity > 0:
        if (manager.account - (quantity * value)) > 0:
            manager.magazynier(identifier, value, quantity)
            manager.account -= (value * quantity)
            manager.zapis_akcji("sprzedaz",[identifier, value, quantity])
            return True
        else:
            print("brak srodkow")
        return False
    else:
        print("Zle dane")
        return False


@manager.assign("konto")
def account(manager, *args, **kwargs):
    a = manager.account
    sl = [{'Obecne Saldo twojego konta to':a}]
    path = "saldo.json"
    with open(path, 'w') as f:
        json.dump(sl,f)


@manager.assign("saldo")
def saldo(manager, accountant_change, *args, **kwargs):
    if manager.account + accountant_change >= 0:
        manager.account += accountant_change


@manager.assign("sprzedaz")
def sprzedaz(manager, identifier, value, quantity, *args, **kwargs):
    if value > 0 and quantity > 0:
        if manager.magazynier(identifier, value, quantity * (-1)):
            manager.account += (value * quantity)
            manager.zapis_akcji("sprzedaz", [identifier, value, quantity])
            return True
        else:
            return False
    else:
        print("Zle dane")
        return False


manager.data_loader()

if __name__ == "__main__":
    print(manager.historia)