import sys
from files import FileHandler
from ZADANIA.Prosty_system_księgowy_magazyn.main import Magazyn

file_path_output = "out.txt"

#read file path from argv
file_path_input = sys.argv[1]

file_handler = FileHandler(file_path_read=file_path_input, file_path_write=file_path_output)
file_handler.read_history()

magazyn = Magazyn(file_handler.history)
magazyn.oblicz_aktualny_stan()

nowa_komenda = sys.argv[2:]

magazyn.wykonaj_komende(nowa_komenda)

magazyn.dopisz_historia(nowa_komenda)
file_handler.write_history(magazyn.historia)


