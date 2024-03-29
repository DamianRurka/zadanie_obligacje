import sys
from files import FileHandler
from ZADANIA.Prosty_system_księgowy_magazyn.main import Magazyn

file_path_output = "out.txt"
file_path_input = sys.argv[1]


historia = FileHandler(file_path_read=file_path_input, file_path_write=file_path_output)
historia.read_history()

magazyn = Magazyn(historia.history)
magazyn.oblicz_aktualny_stan()
magazyn.stan_magazynu()
