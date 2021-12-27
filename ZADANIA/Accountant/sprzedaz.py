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

        @manager.assign('sprzedaz')
        def pozycje():
            ac.sprzedaz(sys.argv[2], int(sys.argv[3]), int(sys.argv[4]))
        manager.execute('sprzedaz')

        @manager.assign('przeglad')
        def przeglad(start_stop=[0, 0]):
            ac.przeglad(start_stop[0], start_stop[1])
        manager.execute('przeglad')
    except FileNotFoundError:
        manager.execute_param('error', "Nie udało się załadować pliku")
        break
    ac.update_db()
    break

manager.execute('show_error')