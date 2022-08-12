class Puppy:
    n_puppies = 0  # number of created puppies

    # define __new__
    def __new__(cls):
        if cls.n_puppies < 10:
            cls.n_puppies += 1
            return super().__new__(cls)
        return None

    def __str__(self):
        return f"{self.n_puppies}"
