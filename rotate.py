from abc import ABC, abstractmethod

from exception import ExceptionHandler
from command import ICommand


class RotableInterface(ABC):
    def __init__(self):
        self.get_direction = 0
        self.get_angular_velocity = 0
        self.get_directions_number = 0

    @abstractmethod
    def set_direction(self):
        pass


class Rotable(ICommand, RotableInterface):
    def set_direction(self):
        self.get_direction = (
            (self.get_direction + self.get_angular_velocity) % self.get_directions_number
        )

    def execute(self):
        try:
            self.set_direction()
        except Exception as e:
            return ExceptionHandler.handle(e, self)
