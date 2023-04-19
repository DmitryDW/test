from pytest_bdd import (given, parsers, when, then)
from les01.app.garage import *
from les01.app.car import *
from les01.app.store import *

store = Store()

@given(parsers.parse('create garage as "{name}"'))
def step_create_garage(name):
    garage = Garage(complect='comfort', power_type='1.6')
    store.set_item(name, garage)
    print(f'Step create garage PASS, new garage with name "{name}" saved in Store')


@given(parsers.parse('create car with name "{name}"'))
def step_create_car(name):
    car = Car(name)
    store.set_item(name, car)
    print(f'Step create car PASS, new car with name "{name}" saved in Store')


@when(parsers.parse('i put car "{car_name}" in garage "{garage_name}"'))
def step_create_car(car_name, garage_name):
    car = store.get_item(car_name)
    garage = store.get_item(garage_name)
    garage.put_car(car)
    print(f'Step put car in garage PASS, new car with name "{car_name}" put in garage "{garage_name}')


@then(parsers.parse('assert that car "{car_name}" in garage "{garage_name}"'))
def step_create_car(car_name, garage_name):
    garage = store.get_item(garage_name)
    assert garage.search_car('name', car_name), f'Car with name "{car_name}" not in garage "{garage_name}"'
    print(f'Step car in garage PASS, car with name "{car_name}" is in the garage "{garage_name}')
