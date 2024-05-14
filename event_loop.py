from command import ICommand


class EventLoop:
    store = []

    @classmethod
    def put(cls, cmd: 'ICommand'):
        cls.store.append(cmd)

    @classmethod
    def get(cls):
        return cls.store.pop(0)

    @classmethod
    def clear(cls):
        cls.store = []
