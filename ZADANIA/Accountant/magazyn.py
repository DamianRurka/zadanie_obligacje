import sys
from MANAGER import manager


identyfikator = sys.argv[2:]   #np.:  magazyn.py "in.txt" "nvidia_geforce" "lenovo" "raspberry"

manager.execute("magazyn", identyfikator)
