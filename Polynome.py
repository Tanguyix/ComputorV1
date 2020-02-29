class Polynome:
    def __init__(self, userEntry):
        self.userEntry = userEntry

    def parse(self):
        monomes = self.userEntry.split('=')
        print(monomes)