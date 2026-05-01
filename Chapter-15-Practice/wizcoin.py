class Wizcoin:
    def __init__(self, galleons, sickles, knuts):
        """Creates a new Wizcoin object with galleons, sickles and knuts"""
        self.galleons = galleons
        self.sickles = sickles
        self.knuts = knuts

    def value(self):
        """The value (in knuts) of all the coins in the Wizcoin object"""
        return (self.galleons *17 * 29) + (self.sickles * 29) + (self.knuts)

    def weightinGrams(self):
        """Returns the weight of the coins"""
        return (self.galleons *31.103) + (self.sickles * 11.34) + (self.knuts * 5.0)

    