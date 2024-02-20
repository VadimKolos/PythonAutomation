class Animal:
    def __init__(self, name):
        self.name = name

    def sound(self):
        return "Any sound"

    def move(self):
        return "Average movement"


class Dog(Animal):
    def __init__(self, name):
        super().__init__(name)

    def sound(self):
        return "Gav!"

    def move(self):
        return "Run"
