import random


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


# Working on getting this to work, being a dictionary at the moment, will change to 2d array


spaces = ['Go', 'Old Kent Road', 'Community Chest', 'Whitechapel Road', 'Income Tax', 'Kings Cross Station',
          f'The Angel Islington', 'Chance', 'Euston Road', 'Pentonville Road', 'Jail', 'Pall Mall', 'Electric Company',
          f'Whitehall', 'Northumberland Avenue', 'Pikmin Station', 'Bow Street', 'Community Chest',
          f'Marlborough street', 'Vine Street', 'Free Parking', 'Strand', 'Chance', 'Fleet Street', 'Trafalgar Square',
          f'Fenchurch Station', 'Leicester Square', 'Coventry Street', 'Water Works', 'Piccadilly', 'Go To Jail',
          f'Regent Street', 'Oxford Street', 'Community Chest', 'Bond Street', 'Liverpool street station', 'Chance',
          f'Park Lane', 'Luxury Tax', 'Mayfair']
Brown = {"Old Kent Road": 60, "Whitechapel": 60}
Lblue = {"The Angel Islington": 100, "Euston Road": 100, "Pentonville Road": 120}
Pink = {"Pall Mall": 140, "Whitehall": 140, "Northumberland Avenue": 160}
Orange = {"Bow Street": 180, "Marlborough Street": 180, "Vine Street": 200}
Red = {"Strand": 220, "Fleet Street": 220, "Trafalgar Square": 240}
Yellow = {"Leicester Square": 260, "Coventry Street": 260, "Piccadilly": 280}
Green = {"Regent Street": 300, "Oxford Street": 300, "Bond Street": 320}
Dblue = {"Park Lane": 350, "Mayfair": 400}
Stations = {"King's Cross Station": 200, "Marylebone Station": 200, "Fenchurch Street Station": 200,
            "Liverpool Street Station": 200}


def rollDice(rollCounter):
    roll1 = random.randint(1, 6)
    roll2 = random.randint(1, 6)
    rollCounter += 1
    total = roll1 + roll2
    if roll1 != roll2:
        print(f'You rolled a {total}! ')
        canRoll = False
        return total
    else:
        print(f'You rolled a double! Move {total} spaces.')
        return total


def moveSpaces(moves, location):
    """Get the current player location index and add the number
    of moves to it. Loop if the index is greater than Mayfair"""
    pass


def GameLoop():
    playerCount = int(input('How many players will there be? '))

    while True:
        for i in range(playerCount):

            rollCounter = 0
            canRoll = True
            while canRoll:
                moves = rollDice(rollCounter)

                pass

    # Roll dice

    # Calculate score

    # Move spaces

    # Check for Go

    # Check for payment

    # Next player

    pass


if __name__ == "__main__":
    GameLoop()
