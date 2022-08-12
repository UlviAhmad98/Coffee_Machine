class Person:
    def __init__(self, name):
        self.name = name

    # create the method greet here
    def greet(self):
        return "Hello, I am {}!".format(self.name)


first_name = input()
person = Person(first_name)
print(person.greet())
