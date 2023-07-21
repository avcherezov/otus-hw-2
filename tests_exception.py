from move import Movable
from object import UObject


object = {
    'position': [12, 5],
    'velosity': [-7, 3],
}


class MovableAdapter(Movable, UObject):
    def __init__(self, object):
        self.object = object
        self.get_position = None
        self.get_velosity = self.get_property('velosity')


move1 = MovableAdapter(object)
move1.execute()
