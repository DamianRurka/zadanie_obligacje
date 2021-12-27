import sys
from action import Account
from action import Manager

manager = Manager()
ac = Account()

@manager.assign("error")
def get_error(take_error):
    manager.error = take_error

@manager.assign('show_error')
def show_err():
    if manager.error:
        print(manager.error)

while True:

    try:
        ac.get_file_path(sys.argv[1])
    except IndexError:
        manager.execute_param('error', 'Brak ścieżki wejścia')
        break
    try:
        ac.import_db()

        @manager.assign('konto')
        def account():
            print(ac.saldo_kwota)
        manager.execute('konto')
    except FileNotFoundError:
        manager.execute_param('error', "błąd ładowania pliku")
        break
    break
manager.execute('show_error')