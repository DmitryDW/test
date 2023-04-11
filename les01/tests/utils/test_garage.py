import pytest
from pytest_bdd import scenario
from les01.tests.steps import *

# KAV-01
@scenario("garage.feature",
          "create garage")
def test_create_garage():
    pass