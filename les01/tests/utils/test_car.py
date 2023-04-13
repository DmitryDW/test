import pytest
from les01.app.car import Car

@pytest.mark.car
def test_car():
    car = Car('skoda')
    assert car.name == 'skoda'


@pytest.mark.car
def test_car_light():
    car = Car('skoda')
    status = car.light()
    assert status == True

    status = car.light()
    assert status == False


@pytest.mark.car
def test_car_engine():
    car = Car('skoda')
    status = car.engine()
    assert status == True

    status = car.engine()
    assert status == False


@pytest.mark.car
def test_car_wipers():
    car = Car('skoda')
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