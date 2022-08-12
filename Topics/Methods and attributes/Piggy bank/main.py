class PiggyBank:
    # create __init__ and add_money methods
    def __init__(self, dollars, cents):
        self.dollars = dollars
        self.cents = cents
        self.paper = None
        self.coin = None

    def add_money(self, deposit_dollars, deposit_cents):
        self.paper = deposit_dollars
        self.coin = deposit_cents
        self.dollars += self.paper
        self.cents += self.coin
        cent = self.cents % 100
        dollar = self.cents // 100
        if dollar != 0:
            self.dollars += dollar
            self.cents = cent


pg = PiggyBank(1, 1)

