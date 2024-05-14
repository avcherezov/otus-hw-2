import os

from move import Movable
from object import UObject
from event_loop import EventLoop
from exception import RepeatCommand, DoubleRepeatCommand, ExceptionLogger, ExceptionHandler

import pytest


@pytest.fixture(autouse=True)
def clear_event_loop():
    EventLoop.clear()


@pytest.fixture(scope='session', autouse=True)
def delete_log():
    pytest.log_file = 'log.log'
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


def test_1():
    ERRORS = {
        'MovableAdapter': {
            'TypeError': RepeatCommand
        },
        'RepeatCommand': {
            'TypeError': ExceptionLogger
        }
    }
    ExceptionHandler.errors = ERRORS

    move = MovableAdapter(object)
    EventLoop.put(move)
    first_command = EventLoop.get().execute()
    assert type(first_command).__name__ == 'RepeatCommand'

    EventLoop.put(first_command)
    repeat_first_command = EventLoop.get().execute(first_command.command)
    assert type(repeat_first_command).__name__ == 'ExceptionLogger'

    EventLoop.put(repeat_first_command)
    EventLoop.get().execute()
    file_list = os.listdir()
    assert pytest.log_file in file_list


def test_2():
    ERRORS = {
        'MovableAdapter': {
            'TypeError': RepeatCommand
        },
        'RepeatCommand': {
            'TypeError': DoubleRepeatCommand
        },
        'DoubleRepeatCommand': {
            'TypeError': ExceptionLogger
        }
    }
    ExceptionHandler.errors = ERRORS

    move = MovableAdapter(object)
    EventLoop.put(move)
    first_command = EventLoop.get().execute()
    assert type(first_command).__name__ == 'RepeatCommand'

    EventLoop.put(first_command)
    repeat_first_command = EventLoop.get().execute(first_command.command)
    assert type(repeat_first_command).__name__ == 'DoubleRepeatCommand'

    EventLoop.put(repeat_first_command)
    double_repeat_first_command = EventLoop.get().execute(first_command.command)
    assert type(double_repeat_first_command).__name__ == 'ExceptionLogger'

    EventLoop.put(double_repeat_first_command)
    EventLoop.get().execute()
    file_list = os.listdir()
    assert pytest.log_file in file_list
