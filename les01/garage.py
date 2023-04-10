class Garage:

    def __init__(self):
        self._places = []

    def put_car(self, car):
        self._places.append(car)

    def put_cars(self, cars):
        for car in cars:
            self.put_car(car)

    def move_car(self, car):
        self._places.remove(car)

    def move_cars(self, cars):
        for car in cars:
            self.move_car(car)

    def search_car(self, attr, request):
        results = []
        for car in self._places:
            value = getattr(car, attr, False)
            if value == request:
                results.append(car)

        return results if results else None
