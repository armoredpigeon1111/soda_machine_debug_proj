from coins import Coin

class Wallet:
    def __init__(self): 
        self.money = []
        self.coins = Coin() # added
        fill_wallet(self)
       


def fill_wallet(self):
    """Method will fill wallet's money list with certain amount of each type of coin when called."""
    for index in range(8):
        self.money.append(self.coins.Quarter()) # added self to these
    for index in range(10):
        self.money.append(self.coins.Dime())
    for index in range(20):
        self.money.append(self.coins.Nickel())
    for index in range(50):
        self.money.append(self.coins.Penny())
