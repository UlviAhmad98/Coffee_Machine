    # def __init__(self):
    #     pass
    #
    # def push(self, el):
    #     pass
    #
    # def pop(self):
    #     pass
    #
    # def peek(self):
    #     pass
    #
    # def is_empty(self):
    #     pass

class Stack:
    def __init__(self):
        self.items = []

    def push(self, el):
        self.items.insert(0, el)

    def pop(self):
        return self.items.pop(0)

    def peek(self):
        return self.items[0]

    def is_empty(self):
        return self.items == []

# s = Stack()
# s.push('hello')
# s.push('true')
# print(s.pop())
