class GoodIfrit:
    def __init__(self, height, name, kidness):
        self.height = height
        self.name = name
        self.kidness = kidness

    def change_goodness(self, value):
        self.kidness += value
        if self.kidness < 0:
            self.kidness = 0

    def __add__(self, number):
        return GoodIfrit(self.height + number, self.name, self.kidness)

    def __str__(self):
        return f'Good Ifrit {self.name}, height {self.height}, goodness {self.kidness}'

    def __call__(self, argument):
        return argument * self.kidness // self.height

    def __eq__(self, other):
        if self.kidness == other.kidness and self.height == other.height and \
                self.name == other.name:
            return True
        return False

    def __lt__(self, other):
        if self.kidness < other.kidness:
            return True
        if self.height < other.height:
            return True
        if self.name < other.name:
            return True
        return False

    def __le__(self, other):
        if self.kidness < other.kidness:
            return True
        if self.height < other.height:
            return True
        if self.name < other.name:
            return True
        if self.name == other.name and \
                self.height == other.height and \
                self.kidness == other.kidness:
            return True
        return False
