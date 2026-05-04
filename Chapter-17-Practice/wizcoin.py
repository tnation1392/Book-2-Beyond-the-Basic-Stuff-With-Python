class WizcoinException(Exception):
    #This will raise when the module is incorrectly used
    pass

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

    @property
    def galleons(self):
        #Returns the number of galleons
        return self.galleons

    @galleons.setter
    def galleons(self, value):
        if not isinstance(value, int):
            raise WizcoinException('galleons must be an integer' + value.__class__.__qualname__)
        if value < 0:
            raise WizcoinException('galleons must be positive' + value.__class__.__qualname__)
        self.galleons = value