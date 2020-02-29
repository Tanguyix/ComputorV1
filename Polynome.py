import sys

class Polynome:
    def __init__(self, userEntry):
        self.userEntry = userEntry
        self.monomes = []

    def parse(self):
        monomes = self.userEntry.split('=')
        if len(monomes) != 2:
            print('format, 1 egal exactement')
            sys.exit()
        self.parseMonome(monomes[0])
        self.parseMonome(monomes[1])
        print(self.monomes)
        
    def parseMonome(self, monome):
        i = -1
        j = -1
        values = []
        while i < len(monome):
            values.append('')
            j += 1
            if monome[i] == '-':
                values[j] = '-'
            i += 1
            while i < len(monome) and monome[i] != '+' and monome[i] != '-':
                values[j] += monome[i]
                i += 1
        self.monomes.append(values)