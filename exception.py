from object import UObject
from command import ICommand
from logger import Logger


class RepeatCommand(ICommand):
    def __init__(self, obj):
        self.command = obj.get_property("command")

    def execute(self, command=None):
        return command.execute(self)


class DoubleRepeatCommand(RepeatCommand):
    pass


class ExceptionLogger(ICommand):
    def __init__(self, obj):
        self.command = obj.get_property("command")
        self.exception_type = obj.get_property("exception_type")

    def execute(self):
        Logger.log(f'Exception - {self.exception_type}, Class - {self.command}')


class MoveErrorException(Exception):
    def __init__(self, obj):
        self.command = obj.get_property("command")
        self.exception_type = obj.get_property("exception_type")

    def __str__(self):
        return "сдвинуть объект не возможно"


class RotateErrorException(Exception):
    def __init__(self, obj):
        self.command = obj.get_property("command")
        self.exception_type = obj.get_property("exception_type")

    def __str__(self):
        return "повернуть объект не возможно"


class FuelErrorException(Exception):
    def __init__(self, obj):
        self.command = obj.get_property("command")
        self.exception_type = obj.get_property("exception_type")

    def __str__(self):
        return "проблема с топливом"


class ExceptionHandler:
    errors = None

    @classmethod
    def _handled(clt, e, c):
        return UObject(
            {
                'exception_type': e,
                'command': c
            }
        )

    @classmethod
    def handle(clt, e, c):
        command = c.__class__.__name__
        exception = e.__class__.__name__

        return clt.errors[command][exception](clt._handled(exception, c))
