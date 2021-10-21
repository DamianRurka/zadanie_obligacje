class ProductPiece:

    def __init__(self, price):
        self.price = price

    def ask(self):
        print("Podaj liczbę sztuk")
        return int(input())

    def print(self, howmuch):
        print("Zamówiono {} liczbę sztuk".format(howmuch))

    def price(self, howmuch):
        return howmuch * self.price


class ProductPack:


    def __init__(self, price, size):
        self.price = price
        self.size = size


    def ask(self):
        print("Podaj liczbę sztuk")
        return int(input())


    def print(self, howmuch):
        packs = int((howmuch + self.size - 1) / self.size)
        print("Zamówiono {} liczbę paczek".format(packs))


    def price(self, howmuch):
        packs = int((howmuch + self.size - 1) / self.size)
        return packs * self.price


class AmountPack:


    def __init__(self, price, loss, unit):
        self.price = price
        self.loss = loss
        self.unit = unit


    def ask(self):
        print("Podaj ilość ({})".format(self.unit))
        return float(input())


    def print(self, howmuch):
        print("Zamówiono {} ({})".format(howmuch, self.unit))


    def price(self, howmuch):
        return self.price * howmuch * (1 + self.loss)
products = {
  "product_floor_tiles_white": ProductPack(120, 15),
  "product_floor_tiles_black": ProductPack(140,20),
  "paint_can": ProductPiece(60),
  "paint_brush": ProductPiece(60),
  "planks": AmountPack(80, 0.1, "metry"),
  "concrete": AmountPack(60, 0.05, "kilogramy")
}

total_price = 0
while True:
    print("Podaj nazwę produktu lub pustą linię jeśli chcesz zakończyć")
    product = input()
    if product not in products:
        print("Błędna nazwa produktu")
        continue
    product = products[product]
  #zapytajmy o wielkość zamówienia
    howmuch = product.ask()
  #wydrukujmy potwierdzenie
    product.print()
  #dodajmy cenę
    total_price += product.price(howmuch)

print("Całkowity koszt zamówienia {}".format(total_price))