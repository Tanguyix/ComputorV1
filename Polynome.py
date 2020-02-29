import sys
import re

class Polynome:
    def __init__(self, userEntry):
        self.userEntry = userEntry
        self.strMonomes = []
        self.monomes = []

    def parse(self):
        monomes = self.userEntry.split('=')
        if len(monomes) != 2:
            print('format, 1 egal exactement')
            sys.exit()
        self.parseMonome(monomes[0])
        self.parseMonome(monomes[1])
        self.getElements(self.strMonomes[0])
        self.getElements(self.strMonomes[1])
        print(self.monomes)
        
    def getElements(self, monome):
        poly = dict()
        for elem in monome:
            degre = 0
            elem = elem.replace(' ', '')
            x = re.search("X\^[0-9]+", elem)
            if x:
                power = x.group()
                degre = re.search("[0-9]+", power)
                degre = degre.group()
            elem = elem.replace('*', '')
            elem = re.sub("X\^[0-9]+", "", elem)
            if str(degre) in poly:
                print("degre in poly")
                poly[str(degre)] += float(elem)
            else:
                poly[degre] = float(elem)
        self.monomes.append(poly)


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
        self.strMonomes.append(values)