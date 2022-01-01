import json
from flask import Flask, render_template, request
import mysql.connector

app = Flask(__name__)


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
    connection = mysql.connector.connect(user='root', password='Wikingowie123x',
                                         host='127.0.0.1', database='accountant',
                                         auth_plugin='mysql_native_password')

    cursorPS = connection.cursor(buffered=True)
    datacheck = "SELECT saldo FROM stankonta WHERE idnew_table = 1"
    cursorPS.execute(datacheck)
    for row in cursorPS:
        Saldok = row
        return render_template('konto.html',Saldok = Saldok)
    connection.close()

@app.route('/magazyn/')
def magazyn():


    connection = mysql.connector.connect(user='root', password='Wikingowie123x',
                                         host='127.0.0.1', database='accountant',
                                         auth_plugin='mysql_native_password')

    cursor = connection.cursor(buffered=True)

    datacheck = "SELECT nazwaproduktu,liczbasztuk FROM magazyndata "
    cursor.execute(datacheck)
    numrows = cursor.rowcount


    for rows in cursor.fetchall():
        content = rows
        print(content)

        return render_template('magazyn.html',content=content)
    connection.close()



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