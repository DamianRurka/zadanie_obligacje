import sys
from MANAGER import manager

start = int(sys.argv[2])
end = int(sys.argv[3])
manager.execute("przeglad", start, end)


