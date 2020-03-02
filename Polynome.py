import sys
import re
from utils import sqrt

class Polynome:
    def __init__(self, userEntry):
        self.userEntry = userEntry
        self.strMonomes = []
        self.monomes = []
        self.degre = 0
        self.reduced = dict()

    def parse(self):
        monomes = self.userEntry.split('=')
        if len(monomes) != 2:
            print('format, 1 egal exactement')
            sys.exit()
        self.parseMonome(monomes[0])
        self.parseMonome(monomes[1])
        self.getElements(self.strMonomes[0])
        self.getElements(self.strMonomes[1])
        
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
                poly[str(degre)] += float(elem)
            elif not len(elem):
                poly[str(degre)] = 1
            else:
                poly[str(degre)] = float(elem)
        self.monomes.append(poly)


    def parseMonome(self, monome):
        i = -1
        j = -1
        values = []
        monome = monome.replace('X ', 'X^1')
        monome = monome.replace('X+', 'X^1')
        monome = monome.replace('X-', 'X^1')
        if monome[len(monome) - 1 ] == 'X':
            monome += '^1'

        while i < len(monome):
            values.append('')
            values[j] = values[j].replace(" ", "")
            j += 1
            if monome[i] == '-':
                values[j] = '-'
            i += 1
            while i < len(monome) and monome[i] != '+' and monome[i] != '-':
                values[j] += monome[i]
                i += 1
        values = list(filter(None, values))
        self.strMonomes.append(values)

    def reduce(self):
        left = self.monomes[0]
        right = self.monomes[1]
        for elem in right:
            if (elem in left): 
                left[str(elem)] -= float(right[elem])
            else:
                left[str(elem)] = -float(right[elem])
        self.reduced = left
        self.printReduced(left)

    def printReduced(self, reduced):
        string = "Reduced form: "
        for i in reduced:
            if (reduced[i]):
                string += (str(reduced[i]) + " * X^" + str(i) + " + ")
        string = string.replace("+ -", "- ")
        string += "= 0"
        string = string.replace("+ =", "=")
        string = string.replace(".0 ", " ")
        print(string)

    def solve(self):
        self.getDegre(self.reduced)
        if (self.degre >= 3):
            print("The polynomial degree is stricly greater than 2, I can't solve.")
            sys.exit()
        elif self.degre == 2:
            self.solveDeg2(self.reduced)
        elif self.degre == 1:
            self.solveDeg1(self.reduced)
        else:
            self.solveDeg0(self.reduced)

    def getDegre(self, reduced):
        self.degre = int(max((reduced.keys()))) 
        print("Polynomial degree: ", self.degre)

    def solveDeg0(self, reduced):
        if (reduced["0"] == 0):
            print("All numbers are solutions")
        else:
            print("No solutions")

    def solveDeg1(self, reduced):
        a = reduced["1"]
        b = reduced["0"]
        print("The solution is:")
        if a: 
            print(-b / a)
        else:
            print(0)
        
    def solveDeg2(self, reduced):
        a = reduced["2"]
        b = reduced["1"]
        c = reduced["0"]
        delta = b * b - 4 * a * c

        if delta < 0:
            sqr = sqrt(-delta, 0.001)
            print("Discriminand is strictly negative, the 2 complex solutions are:")
            print("(", -b, " + ", sqr, "i ) /", 2 * a)
            print("(", -b, " - ", sqr, "i ) /", 2 * a)
        elif delta == 0:
            print("Discriminant is equal to zero, the solution is:")
            print(-b / (2 * a))
        else:
            sqr = sqrt(delta, 0.001)
            print("Discriminant is strictly positive, the 2 solutions are:")
            print((-b + sqr) / (2 * a))
            print((-b - sqr) / (2 * a))

