from fuel import CheckFuel, BurnFuel, CommandException
from object import UObject
from exception import FuelErrorException, ExceptionHandler


ERRORS = {
    'BurnFuelAdapter': {
        'TypeError': FuelErrorException
    },
}
ExceptionHandler.errors = ERRORS


object = {
    'fuel_amount': [10],
    'fuel_burn_rate': 2
}


def test_1():
    class CheckFuelAdapter(CheckFuel, UObject):
        def __init__(self, object):
            self.object = object
            self.get_fuel_amount = self.get_property('fuel_amount')
            self.get_fuel_burn_rate = self.get_property('fuel_burn_rate')

    check = CheckFuelAdapter(object)
    check.execute()


def test_2():
    object = {
        'fuel_amount': [10],
        'fuel_burn_rate': 20
    }

    class CheckFuelAdapter(CheckFuel, UObject):
        def __init__(self, object):
            self.object = object
            self.get_fuel_amount = self.get_property('fuel_amount')
            self.get_fuel_burn_rate = self.get_property('fuel_burn_rate')

    check = CheckFuelAdapter(object)
    try:
        check.execute()
    except CommandException:
        assert True


def test_3():
    class BurnFuelAdapter(BurnFuel, UObject):
        def __init__(self, object):
            self.object = object
            self.get_fuel_amount = self.get_property('fuel_amount')
            self.get_fuel_burn_rate = self.get_property('fuel_burn_rate')

    fuel = BurnFuelAdapter(object)
    fuel.execute()

    assert fuel.get_fuel_amount[0] == 8


def test_4():
    class BurnFuelAdapter(BurnFuel, UObject):
        def __init__(self, object):
            self.object = object
            self.get_fuel_amount = None
            self.get_fuel_burn_rate = self.get_property('fuel_burn_rate')

    fuel = BurnFuelAdapter(object)
    error = fuel.execute()

    assert isinstance(error, Exception)
    assert error.__str__() == 'проблема с топливом'


def test_5():
    class BurnFuelAdapter(BurnFuel, UObject):
        def __init__(self, object):
            self.object = object
            self.get_fuel_amount = self.get_property('fuel_amount')
            self.get_fuel_burn_rate = None

    fuel = BurnFuelAdapter(object)
    error = fuel.execute()

    assert isinstance(error, Exception)
    assert error.__str__() == 'проблема с топливом'
