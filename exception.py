ERRORS = {
    'MovableAdapter': {
        'TypeError': 'сдвинуть объект не возможно'
    }
}


class ExceptionHandler:
    errors = ERRORS

    @classmethod
    def handle(clt, e, c):
        command = c.__class__.__name__
        exception = e.__class__.__name__

        raise Exception(clt.errors[command][exception])
