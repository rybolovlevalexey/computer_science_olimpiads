class Animal:
    def __init__(self, name):
        self.name = name

    def make_sound(self):
        print(self.name + " says " + self.sound)

    def move(self):
        raise NotImplementedError()


class Dog(Animal):
    def __init__(self, name):
        super.__init__(name)
        self.sound = 'woof'
    def move(self):
        return f'{self.name} walks'


class Snake(Animal):
    def __init__(self, name):
        super.__init__(name)
        self.sound = 'hsss'
    def move(self):
        return f'{self.name} crawles'