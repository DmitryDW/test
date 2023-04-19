class Garage:
    color = 'red'
    size = 1145

    place = []

    def __init__(self, complect, power_type):
        self.complect = complect
        self.power_type = power_type

    @classmethod
    def set_place(cls, auto):
        cls.place.append(auto)

    @classmethod
    def set_places(cls, autos):
        for obj in autos:
            cls.place.append(obj)


autos = Garage('complect', 'power_type')
autos.set_places(['skoda', 'uaz', 'kia', 'lada'])

skoda = Garage('comfort', 'tdi_1.3')
lada = Garage('comfort', 'tfs_1.4')
uaz = Garage('standart', 'tdi_2.5')
kia = Garage('standart', 'tfs_1.6')
toyota = Garage('premium', 'tdi_2.0')

table = Garage.set_place(Garage)

print(autos)
print(table)