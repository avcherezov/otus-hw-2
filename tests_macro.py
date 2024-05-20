from object import UObject
from move import Movable
from fuel import CheckFuel, BurnFuel, CommandException
from macro_commands import MoveAndBurnFuel


class MovableAdapter(Movable, UObject):
    def __init__(self, object):
        self.object = object
        self.get_position = self.get_property('position')
        self.get_velosity = self.get_property('velosity')


class CheckFuelAdapter(CheckFuel, UObject):
    def __init__(self, object):
        self.object = object
        self.get_fuel_amount = self.get_property('fuel_amount')
        self.get_fuel_burn_rate = self.get_property('fuel_burn_rate')


class BurnFuelAdapter(BurnFuel, UObject):
    def __init__(self, object):
        self.object = object
        self.get_fuel_amount = self.get_property('fuel_amount')
        self.get_fuel_burn_rate = self.get_property('fuel_burn_rate')


class MoveAndBurnFuelAdapter(MoveAndBurnFuel, UObject):
    def __init__(self, object):
        self.object = object
        self.get_position = self.get_property('position')
        self.get_velosity = self.get_property('velosity')
        self.get_fuel_amount = self.get_property('fuel_amount')
        self.get_fuel_burn_rate = self.get_property('fuel_burn_rate')
        MoveAndBurnFuel.__init__(
            self, CheckFuelAdapter(self.object), MovableAdapter(self.object), BurnFuelAdapter(self.object)
        )


def test_1():
    object = {
        'position': [12, 5],
        'velosity': [-7, 3],
        'fuel_amount': [10],
        'fuel_burn_rate': 2
    }
    move = MoveAndBurnFuelAdapter(object)
    move.execute()

    assert move.get_position == [5, 8] and move.get_fuel_amount[0] == 8


def test_2():
    object = {
        'position': [12, 5],
        'velosity': [-7, 3],
        'fuel_amount': [10],
        'fuel_burn_rate': 20
    }
    move = MoveAndBurnFuelAdapter(object)
    try:
        move.execute()
    except CommandException:
        assert True
