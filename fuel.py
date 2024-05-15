from abc import ABC, abstractmethod

from exception import ExceptionHandler
from command import ICommand


class CommandException(Exception):
    pass


class CheckFuelInterface(ABC):
    def __init__(self):
        self.get_fuel_amount = []
        self.get_fuel_burn_rate = 0

    @abstractmethod
    def check(self):
        pass


class CheckFuel(ICommand, CheckFuelInterface):
    def check(self):
        if self.get_fuel_burn_rate > self.get_fuel_amount[0]:
            raise CommandException

    def execute(self):
        self.check()


class BurnFuelInterface(ABC):
    def __init__(self):
        self.get_fuel_amount = []
        self.get_fuel_burn_rate = 0

    @abstractmethod
    def set_fuel_amount(self):
        pass


class BurnFuel(ICommand, BurnFuelInterface):
    def set_fuel_amount(self):
        self.get_fuel_amount[0] -= self.get_fuel_burn_rate

    def execute(self):
        try:
            self.set_fuel_amount()
        except Exception as e:
            return ExceptionHandler.handle(e, self)
