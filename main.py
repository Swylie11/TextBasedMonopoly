class Space:
    def __init__(self, name, index):
        self.name = name
        self.index = index


class Player:
    def __init__(self, name, location, properties, balance=1500, jailed=False):
        self.name = name
        self.balance = balance
        self.location = location
        self.properties = properties
        self.jailed = jailed

    def makePayment(self, amount):
        self.balance += amount


class Property(Space):
    def __init__(self, name, index, colour, value, owner, penaltyValue, owned=False):
        super().__init__(name, index)
        self.name = name
        self.colour = colour
        self.value = value
        self.owner = owner
        self.penaltyValue = penaltyValue
        self.owned = owned


class Chance(Space):
    def __init__(self, name, index):
        super().__init__(name, index)

    def generateCard(self):
        pass


class Station(Space):
    def __init__(self, name, index, price, owner, isOwned=False):
        super().__init__(name, index)
        self.name = name
        self.index = index
        self.price = price
        self.owner = owner
        self.isOwned = isOwned


class CommunityChest(Space):
    def __init__(self, name, index):
        super().__init__(name, index)

    def generateCard(self):
        pass


class Go(Space):
    def __init__(self, name, index, payout=False):
        super().__init__(name, index)
        self.name = name
        self.index = index
        self.payout = payout


class FreeParking(Space):
    def __init__(self, name, index):
        super().__init__(name, index)
        self.name = name
        self.index = index


class Utilities(Space):
    def __init__(self, name, index, cost=150, isOwned=False):
        super().__init__(name, index)
        self.name = name
        self.index = index
        self.cost = cost
        self.isOwned = isOwned


class Jail(Space):
    def __init__(self, name, index, timeServable, bail):
        super().__init__(name, index)
        self.name = name
        self.timeServable = timeServable
        self.bail = bail


class GoToJail(Space):
    def __init__(self, name, index):
        super().__init__(name, index)
        self.name = name
        self.index = index


spaces = ['Go', 'Old Kent Road', 'Community Chest', 'Whitechapel Road', 'Income Tax', 'Kings Cross Station',
          f'The Angel Islington', 'Chance', 'Euston Road', 'Pentonville Road', 'Jail', 'Pall Mall', 'Electric Company',
          f'Whitehall', 'Northumberland Avenue', 'Marylebone Station', 'Bow Street', 'Community Chest',
          f'Marlborough street', 'Vine Street', 'Free Parking', 'Strand', 'Chance', 'Fleet Street', 'Trafalgar Square',
          f'Fenchurch Station', 'Leicester Square', 'Coventry Street', 'Water Works', 'Piccadilly', 'Go To Jail',
          f'Regent Street', 'Oxford Street', 'Community Chest', 'Bond Street', 'Liverpool street station', 'Chance',
          f'Park Lane', 'Luxury Tax', 'Mayfair']


def GameLoop():

    # While true

    # Roll dice

    # Calculate score

    # Move spaces

    # Check for payment

    # Next player

    pass


if __name__ == "__main__":
    GameLoop()