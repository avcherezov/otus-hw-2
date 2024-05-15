from abc import ABC, abstractmethod

from command import ICommand


class MacroCommandInterface(ABC):
    def __init__(self, *args):
        self.object = args

    @abstractmethod
    def execute(self):
        pass


class MoveAndBurnFuel(ICommand, MacroCommandInterface):
    def execute(self):
        for cmd in self.object:
            cmd.execute()
