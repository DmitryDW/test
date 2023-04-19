import pytest
from les01.app.car import Car
import les01.tests.utils as util


@pytest.mark.car
def test_car(car):
    assert car.name == 'skoda'


@pytest.mark.car
def test_car_light(car):
    status = car.light()
    assert status == True

    status = car.light()
    assert status == False


@pytest.mark.car
def test_car_engine(car):
    status = car.engine()
    assert status == True

    status = car.engine()
    assert status == False


@pytest.mark.car
def test_car_wipers(car):
    assert car._wipers == 0

    car.wipers(1)
    assert car._wipers == 1

    car.wipers(1)
    assert car._wipers == 2

    car.wipers(1)
    assert car._wipers == 3

    car.wipers(1)
    assert car._wipers == 3

    car.wipers(0)
    assert car._wipers == 0