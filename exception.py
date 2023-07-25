class MoveErrorException(Exception):
    def __str__(self):
        return "сдвинуть объект не возможно"


class RotateErrorException(Exception):
    def __str__(self):
        return "повернуть объект не возможно"


ERRORS = {
    'MovableAdapter': {
        'TypeError': MoveErrorException()
    },
    'RotableAdapter': {
        'TypeError': RotateErrorException()
    }
}


class ExceptionHandler:
    errors = ERRORS

    @classmethod
    def handle(clt, e, c):
        command = c.__class__.__name__
        exception = e.__class__.__name__

        return clt.errors[command][exception]
