from abc import ABC, abstractmethod


class RotableInterface(ABC):
    def __init__(self):
        self.get_direction = 0
        self.get_angular_velocity = 0
        self.get_directions_number = 0

    @abstractmethod
    def set_direction(self):
        pass


class Rotable(RotableInterface):
    def set_direction(self):
        try:
            self.get_direction = (
                (self.get_direction + self.get_angular_velocity) % self.get_directions_number
            )
        except:
            self.get_direction = Exception('повернуть объект не возможно')

    def execute(self):
        self.set_direction()
