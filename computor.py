import sys
from Polynome import Polynome

if len(sys.argv) == 1:
    print('inserer usage')
    sys.exit()
userEntry = sys.argv[1]

poly = Polynome(userEntry)
poly.parse()
poly.reduce()
poly.solve()