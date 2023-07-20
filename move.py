from abc import ABC, abstractmethod


class MovableInterface(ABC):
    def __init__(self):
        self.get_position = []
        self.get_velosity = []

    @abstractmethod
    def set_position(self):
        pass


class Movable(MovableInterface):
    def set_position(self):
        try:
            self.get_position[0] += self.get_velosity[0]
            self.get_position[1] += self.get_velosity[1]
        except:
            self.get_position = Exception('сдвинуть объект не возможно')

    def execute(self):
        self.set_position()
