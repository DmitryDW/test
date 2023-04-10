class Car:

    def __init__(self, name):
        self.name = name
        self.power = None
        self.color = None
        self.category = None

        self._engine = False
        self._wipers = 0
        self._light = False

    def engine(self):
        self._engine = not self._engine
        return self._engine

    def wipers(self, switch):
        if not switch:
            self._wipers = 0
        elif self._wipers <= 3:
            self._wipers += 1

        return self._wipers

    def light(self):
        self._light = not self._light
        return self._light
