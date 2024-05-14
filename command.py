from abc import ABC, abstractmethod


class ICommand(ABC):
    @abstractmethod
    def execute(self, command=None, exception_class=None):
        pass
