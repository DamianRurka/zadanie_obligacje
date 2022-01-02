
from flask import Flask, render_template, request
import mysql.connector

app = Flask(__name__)


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
    cursorPS.close()
    if connection.is_connected():
        cursorPS.close()
        connection.close()

@app.route('/przeglad/',methods=['GET','POST'])
def przeglad():
    content = ()
    if request.method == "POST":
        start = int(request.form["starter"])
        end = int(request.form["ender"])
        connection = mysql.connector.connect(user='root', password='Wikingowie123x',
                                             host='127.0.0.1', database='accountant',
                                             auth_plugin='mysql_native_password')

        cursorPS = connection.cursor(buffered=True)
        productnumbercheck = (start,end,)
        datanumbercheck = "SELECT wartosc, komentarz, type FROM saldohistoria LIMIT %s, %s "
        cursorPS.execute(datanumbercheck, productnumbercheck)

        for row in cursorPS:
            content += row

        connection.commit()
        connection.close()
        if connection.is_connected():
            cursorPS.close()
            connection.close()


    return render_template('przeglad.html', content=content)

@app.route('/magazyn/')
def magazyn():
    stanmagazynu = ()
    connection = mysql.connector.connect(user='root', password='Wikingowie123x',
                                         host='127.0.0.1', database='accountant',
                                         auth_plugin='mysql_native_password')

    cursorPS = connection.cursor(buffered=True)

    datacheck = "SELECT nazwaproduktu,liczbasztuk FROM magazyndata "
    cursorPS.execute(datacheck)

    for row in cursorPS:
        stanmagazynu += row

    connection.commit()
    connection.close()
    if connection.is_connected():
        cursorPS.close()
        connection.close()

    return render_template('magazyn.html',content=stanmagazynu)


@app.route('/saldo/',methods=['GET','POST'])
def saldo():
    connection = mysql.connector.connect(user='root', password='Wikingowie123x',
                                         host='127.0.0.1', database='accountant',
                                         auth_plugin='mysql_native_password')

    cursorPS = connection.cursor(buffered=True)
    datacheck = "SELECT saldo FROM stankonta WHERE idnew_table = 1"
    cursorPS.execute(datacheck)
    saldopush=0
    for row in cursorPS:
        Saldok = int(row[0])
        saldopush += Saldok
    if request.method == "POST":
        wartosc = int(request.form["kasaa"])
        komentarz = str(request.form["koment"])
        saldopush += wartosc
        nowystan = (saldopush,)
        moneyupdate = "UPDATE stankonta set saldo = %s WHERE idnew_table = 1"
        cursorPS.execute(moneyupdate,nowystan)
        insertQuery = "INSERT INTO saldohistoria (wartosc, komentarz, type" \
                      " ) VALUES (%(wartosc)s, %(komentarz)s, %(type)s)"

        insertData = {'wartosc': wartosc,
                      'komentarz': komentarz,
                      'type': 'saldo'}

        cursorPS.execute(insertQuery, insertData)
        connection.commit()
        connection.close()
        if connection.is_connected():
            cursorPS.close()
            connection.close()

    return render_template('saldo.html',title='xxx')

@app.route('/zakup/',methods=['GET','POST'])
def zakup():
    connection = mysql.connector.connect(user='root', password='Wikingowie123x',
                                         host='127.0.0.1', database='accountant',
                                         auth_plugin='mysql_native_password')

    cursorPS = connection.cursor(buffered=True)
    datacheck = "SELECT saldo FROM stankonta WHERE idnew_table = 1"
    cursorPS.execute(datacheck)
    saldopush = 0
    content = ()
    for row in cursorPS:
        Saldok = int(row[0])
        saldopush += Saldok
    if request.method == "POST":
        identyfikator = request.form["ident"]
        cena_sztuki = int(request.form["cenas"])
        liczba_sztuk = int(request.form["liczbas"])
        wartosc = cena_sztuki * liczba_sztuk
        if wartosc > saldopush:
            content = "brak środków do zakupu przedmiotów"
            pass
        else:
            productcheck = (identyfikator,)
            datacheck = "SELECT nazwaproduktu FROM magazyndata WHERE nazwaproduktu=%s"
            cursorPS.execute(datacheck, productcheck)
            idx = ()
            for row in cursorPS:
                idx += row
            if identyfikator not in idx:
                saldopush -= wartosc
                nowystan = (saldopush,)
                moneyupdate = "UPDATE stankonta set saldo = %s WHERE idnew_table = 1"
                cursorPS.execute(moneyupdate, nowystan)
                insertQuery = "INSERT INTO magazyndata (nazwaproduktu, liczbasztuk" \
                              " ) VALUES (%(nazwaproduktu)s, %(liczbasztuk)s)"

                insertData = {'nazwaproduktu': identyfikator,
                              'liczbasztuk': liczba_sztuk}

                cursorPS.execute(insertQuery, insertData)
                inserthistory ="INSERT INTO saldohistoria (wartosc, komentarz, type" \
                              " ) VALUES (%(wartosc)s, %(komentarz)s,  %(type)s)"
                inserthistorydata ={'wartosc': wartosc,
                              'komentarz':identyfikator,
                                'type':'zakup'}
                cursorPS.execute(inserthistory, inserthistorydata)

                connection.commit()
                connection.close()
                if connection.is_connected():
                    cursorPS.close()
                    connection.close()

            elif identyfikator in idx:
                productnumbercheck = (identyfikator,)
                datanumbercheck = "SELECT liczbasztuk FROM magazyndata WHERE nazwaproduktu=%s"
                cursorPS.execute(datanumbercheck, productnumbercheck)
                idxnumber = ()
                for row in cursorPS:
                    idxnumber += row

                suma_magazyn_zakup = idxnumber[0] + liczba_sztuk
                saldopush -= wartosc
                nowystan = (saldopush,)
                moneyupdate = "UPDATE stankonta set saldo = %s WHERE idnew_table = 1"
                cursorPS.execute(moneyupdate, nowystan)
                insertQuery = "UPDATE magazyndata set liczbasztuk = %s WHERE nazwaproduktu = %s"
                insertData = (suma_magazyn_zakup,identyfikator,)

                cursorPS.execute(insertQuery, insertData)
                inserthistory = "INSERT INTO saldohistoria (wartosc, komentarz, type" \
                                " ) VALUES (%(wartosc)s, %(komentarz)s,  %(type)s)"
                inserthistorydata = {'wartosc': wartosc,
                                     'komentarz': identyfikator,
                                     'type': 'zakup'}
                cursorPS.execute(inserthistory, inserthistorydata)

                connection.commit()
                connection.close()
                if connection.is_connected():
                    cursorPS.close()
                    connection.close()


    return render_template('zakup.html', content=content)

@app.route('/sprzedaz/',methods=['GET','POST'])
def sprzedaz():
    connection = mysql.connector.connect(user='root', password='Wikingowie123x',
                                         host='127.0.0.1', database='accountant',
                                         auth_plugin='mysql_native_password')

    cursorPS = connection.cursor(buffered=True)
    datacheck = "SELECT saldo FROM stankonta WHERE idnew_table = 1"
    cursorPS.execute(datacheck)
    saldopush = 0
    content = ()
    for row in cursorPS:
        Saldok = int(row[0])
        saldopush += Saldok
    if request.method == "POST":
        identyfikator = request.form["identt"]
        cena_sztuki = int(request.form["cenass"])
        liczba_sztuk = int(request.form["liczbass"])
        wartosc = cena_sztuki * liczba_sztuk
        productcheck = (identyfikator,)
        datacheck = "SELECT nazwaproduktu FROM magazyndata WHERE nazwaproduktu=%s"
        cursorPS.execute(datacheck, productcheck)
        idx=()
        for row in cursorPS:
            idx += row
        if identyfikator not in idx:
            content =  "brak takiego przedmiotu"
            pass
        else:
            productnumbercheck = (identyfikator,)
            datanumbercheck = "SELECT liczbasztuk FROM magazyndata WHERE nazwaproduktu=%s"
            cursorPS.execute(datanumbercheck, productnumbercheck)
            idxnumber=()
            for row in cursorPS:
                idxnumber += row
            if liczba_sztuk > idxnumber[0]:
                content ="brak wystarczającej ilości przedmiotów "
                pass

            else:
                saldopush += wartosc
                nowystan = (saldopush,)
                moneyupdate = "UPDATE stankonta set saldo = %s WHERE idnew_table = 1"
                cursorPS.execute(moneyupdate, nowystan)
                updatenumber = idxnumber[0] - liczba_sztuk

                insertData = (updatenumber,identyfikator,)
                insertQuery = "UPDATE magazyndata set liczbasztuk = %s WHERE nazwaproduktu=%s"

                cursorPS.execute(insertQuery, insertData)
                inserthistory = "INSERT INTO saldohistoria (wartosc, komentarz, type" \
                                " ) VALUES (%(wartosc)s, %(komentarz)s,  %(type)s)"
                inserthistorydata = {'wartosc': wartosc,
                                     'komentarz': identyfikator,
                                     'type': 'sprzedaz'}
                cursorPS.execute(inserthistory, inserthistorydata)

                connection.commit()
                connection.close()
                if connection.is_connected():
                    cursorPS.close()
                    connection.close()

    return render_template('sprzedaz.html', content=content)

