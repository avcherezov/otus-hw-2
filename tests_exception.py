import os

from move import Movable
from object import UObject
from command import Command, Command2

import pytest


@pytest.fixture
def delete_log():
    pytest.log_file = 'test.txt'
    yield
    os.remove(pytest.log_file)


object = {
    'position': [12, 5],
    'velosity': [-7, 3],
}


class MovableAdapter(Movable, UObject):
    def __init__(self, object):
        self.object = object
        self.get_position = None
        self.get_velosity = self.get_property('velosity')


def test_1(delete_log):
    error = 'Ошибка - сдвинуть объект не возможно\n'

    move = MovableAdapter(object)
    array_command = [move]
    command = Command(pytest.log_file)
    command.run_command(array_command)

    file_list = os.listdir()
    assert pytest.log_file in file_list

    with open(pytest.log_file, "r") as f:
        text = f.read()
    assert text in error


def test_2(delete_log):
    error = 'Ошибка - сдвинуть объект не возможно\n'

    move = MovableAdapter(object)
    array_command = [move]
    command = Command2(pytest.log_file)
    command.run_command(array_command)

    file_list = os.listdir()
    assert pytest.log_file in file_list

    with open(pytest.log_file, "r") as f:
        text = f.read()
    assert text in error
