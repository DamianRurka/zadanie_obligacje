import os
import sys
from files import FileHandler
from magazyn import Magazyn

BASE_FOLDER = 'zadanie_magazyn_import'
FILE_INPUT = 'in.txt'
FILE_OUTPUT = 'out_2.txt'

file_path_output = os.path.join(BASE_FOLDER, FILE_OUTPUT)

#   argv
file_path_input = sys.argv[1]

file_handler = FileHandler(file_path_read=file_path_input, file_path_write=file_path_output)
file_handler.read_history()

magazyn = Magazyn(file_handler.history)
magazyn.oblicz_aktualny_stan()

print(magazyn.stan_konta)
print(magazyn.stan_magazynowy)
#file_handler.write_history()

