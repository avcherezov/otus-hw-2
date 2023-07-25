class UObject:
    def __init__(self, object):
        self.object = object

    def get_property(self, key):
        return self.object[key]

    def set_property(self, key, value):
        self.object[key] = value
