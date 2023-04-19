import pytest

from les01 import *
from les02 import *
from les01.app.car import Car


@pytest.fixture(name="car")
def car_afdsfsd_asfdsf():
    return Car('skoda')


@pytest.fixture(autouse=True, scope="function")
def set_wipers():
    print("dasdasd")
