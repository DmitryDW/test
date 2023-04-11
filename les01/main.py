from app.car import Car
from app.garage import Garage


skoda = Car('skoda')

garage = Garage()
garage.put_car(skoda)


print(skoda.__dict__)
print(garage.__dict__)
