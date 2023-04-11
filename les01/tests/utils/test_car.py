import pytest
from les01.app.car import Car

def test_car():
    car = Car('skoda')
    assert car.name == 'skoda'