class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def dist(self, p2):
        return pow(pow((self.x - p2.x), 2) + pow((self.y - p2.y), 2), 0.5)
