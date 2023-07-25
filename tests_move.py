from move import Movable
from object import UObject


object = {
    'position': [12, 5],
    'velosity': [-7, 3],
}


def test_1():
    class MovableAdapter(Movable, UObject):
        def __init__(self, object):
            self.object = object
            self.get_position = self.get_property('position')
            self.get_velosity = self.get_property('velosity')

    move = MovableAdapter(object)
    move.execute()

    assert move.get_position == [5, 8]


def test_2():
    class MovableAdapter(Movable, UObject):
        def __init__(self, object):
            self.object = object
            self.get_position = None
            self.get_velosity = self.get_property('velosity')

    move = MovableAdapter(object)
    error = move.execute()

    assert isinstance(error, Exception)
    assert error.args[0] == 'сдвинуть объект не возможно'


def test_3():
    class MovableAdapter(Movable, UObject):
        def __init__(self, object):
            self.object = object
            self.get_position = self.get_property('position')
            self.get_velosity = None

    move = MovableAdapter(object)
    error = move.execute()

    assert isinstance(error, Exception)
    assert error.args[0] == 'сдвинуть объект не возможно'


def test_4():
    class MovableAdapter(Movable, UObject):
        def __init__(self, object):
            self.object = object
            self.get_position = self.get_property('position')
            self.get_velosity = self.get_property('velosity')

        def set_position(self):
            self.get_position = Exception('сдвинуть объект не возможно')

    move = MovableAdapter(object)
    move.execute()

    assert isinstance(move.get_position, Exception)
    assert move.get_position.args[0] == 'сдвинуть объект не возможно'
