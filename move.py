from abc import ABC, abstractmethod

from exception import ExceptionHandler
from command import ICommand


class MovableInterface(ABC):
    def __init__(self):
        self.get_position = []
        self.get_velosity = []

    @abstractmethod
    def set_position(self):
        pass


class Movable(ICommand, MovableInterface):
    def set_position(self):
        self.get_position[0] += self.get_velosity[0]
        self.get_position[1] += self.get_velosity[1]

    def execute(self, exception_class=None):
        if exception_class is None:
            exception_class = self

        try:
            self.set_position()
        except Exception as e:
            return ExceptionHandler.handle(e, exception_class)
