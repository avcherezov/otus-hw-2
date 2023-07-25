from rotate import Rotable
from object import UObject


object = {
    'direction': 100,
    'angular_velocity': 150,
    'directions_number': 360,
}


def test_1():
    class RotableAdapter(Rotable, UObject):
        def __init__(self, object):
            self.object = object
            self.get_direction = self.get_property('direction')
            self.get_angular_velocity = self.get_property('angular_velocity')
            self.get_directions_number = self.get_property('directions_number')

    rotate = RotableAdapter(object)
    rotate.execute()

    assert rotate.get_direction == 250


def test_2():
    class RotableAdapter(Rotable, UObject):
        def __init__(self, object):
            self.object = object
            self.get_direction = None
            self.get_angular_velocity = self.get_property('angular_velocity')
            self.get_directions_number = self.get_property('directions_number')

    rotate = RotableAdapter(object)
    error = rotate.execute()

    assert isinstance(error, Exception)
    assert error.args[0] == 'повернуть объект не возможно'


def test_3():
    class RotableAdapter(Rotable, UObject):
        def __init__(self, object):
            self.object = object
            self.get_direction = self.get_property('direction')
            self.get_angular_velocity = None
            self.get_directions_number = self.get_property('directions_number')

    rotate = RotableAdapter(object)
    error = rotate.execute()

    assert isinstance(error, Exception)
    assert error.args[0] == 'повернуть объект не возможно'
