import json
from flask import Flask, render_template, request

app = Flask(__name__)

class KONTO():
    from MANAGER import manager
    manager.execute("konto")
    manager.zapis()

class loaderKonto():
    def __init__(self):
        self.path = 'saldo.json'
        self.db_content = {}

    def read_db(self):
        with open(self.path, 'r') as f:
            self.db_content = json.load(f)
        return self.db_content

class Magazyn:
    def __init__(self):
        self.path = 'magazyn.txt'
        self.db_content = {}

    def read_db(self):
        with open(self.path, 'r') as f:
            self.db_content = f.read()
        return self.db_content

class przeglad:
    def __init__(self):
        self.path = 'przeglad.txt'
        self.db_content = {}

    def read_db(self):
        with open(self.path, 'r') as f:
            self.db_content = f.read()
        return self.db_content

@app.route('/')
def main():
    return "Przejdź na : http://127.0.0.1:5000/index/"

@app.route('/index/')
def index():
    return render_template('index.html')

@app.route('/konto/')
def konto():
    KONTO()
    db =  loaderKonto()
    content = db.read_db()
    Saldok = content[0:]
    return render_template('konto.html',Saldok = Saldok)

@app.route('/magazyn/',methods=['GET','POST'])
def magazyn():
    if request.method == "POST":
        raz = request.form["pierwszy"]
        dwa = request.form["drugi"]
        trzy = request.form["trzeci"]
        cztery = request.form["czwarty"]
        piec = request.form["piąty"]
        from MANAGER import manager

        identyfikator = (raz,dwa,trzy,cztery,piec)  # np.:  magazyn.py "in.txt" "nvidia_geforce" "lenovo" "raspberry"
        manager.execute("magazyn", identyfikator)
        title = 'Przedmioty:'
        db = Magazyn()
        content = db.read_db()
        return render_template('magazyn.html',title=title,content=content)
    return render_template('magazyn.html',title='xxx')


@app.route('/przeglad/',methods=['GET','POST'])
def przeglad():
    if request.method == "POST":
        start = request.form["starter"]
        end = request.form["ender"]
        from MANAGER import manager
        manager.execute("przeglad", start, end)
        db = przeglad()
        content = db.read_db()
        return render_template('przeglad.html',content=content)
    return render_template('przeglad.html', title='xxx')

@app.route('/saldo/',methods=['GET','POST'])
def saldo():
    if request.method == "POST":
        wartosc = request.form["kasaa"]
        komentarz = request.form["koment"]
        print(wartosc,komentarz)
        from MANAGER import manager
        manager.execute("saldo", int(wartosc), komentarz)
        manager.zapis("saldo", wartosc, komentarz)
    return render_template('saldo.html',title='xxx')

@app.route('/zakup/',methods=['GET','POST'])
def zakup():
    if request.method == "POST":
        identyfikator = request.form["ident"]
        cena_sztuki = request.form["cenas"]
        liczba_sztuk = request.form["liczbas"]
        from MANAGER import manager
        manager.execute("zakup", identyfikator, int(cena_sztuki), int(liczba_sztuk))
        manager.zapis("zakup", identyfikator, cena_sztuki, liczba_sztuk)
    return render_template('zakup.html')

@app.route('/sprzedaz/',methods=['GET','POST'])
def sprzedaz():
    if request.method == "POST":
        identyfikator = request.form["identt"]
        cena_sztuki = request.form["cenass"]
        liczba_sztuk = request.form["liczbass"]
        from MANAGER import manager
        manager.execute("sprzedaz", identyfikator, int(cena_sztuki), int(liczba_sztuk))
        manager.zapis("sprzedaz", identyfikator, cena_sztuki, liczba_sztuk)
    return render_template('sprzedaz.html')