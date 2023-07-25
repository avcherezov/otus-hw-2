from abc import ABC, abstractmethod

from exception import ExceptionHandler


class MovableInterface(ABC):
    def __init__(self):
        self.get_position = []
        self.get_velosity = []

    @abstractmethod
    def set_position(self):
        pass


class Movable(MovableInterface):
    def set_position(self):
        self.get_position[0] += self.get_velosity[0]
        self.get_position[1] += self.get_velosity[1]

    def execute(self):
        try:
            self.set_position()
        except Exception as e:
            return ExceptionHandler.handle(e, self)
