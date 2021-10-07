class Artist:
    def __init__(self, name = 'None', birthYear = 0, deathYear = 0):
        self.name = name
        self.BirthYear = birthYear
        self.deathYear = deathYear
    def printInfo(self):
        if self.deathYear == str('alive'):
            print('Artist: {}, born {}'.format(self.name, self.BirthYear))
        else:
            print('Artist: {} ({}-{})'.format(self.name, self.BirthYear, self.deathYear))