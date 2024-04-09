from collections import OrderedDict


class LRUCache(OrderedDict):
    def __init__(self, capacity: int = 10):
        self.capacity = capacity
        OrderedDict.__init__(self)

    def get(self, key: str):
        try:
            value = OrderedDict.__getitem__(self, key)
        except KeyError:
            return ""

        return self.__move_on_top(key, value)

    def set(self, key: str, value: str):
        self.__move_on_top(key, value)

    def rem(self, key: str):
        self.__delitem__(key)

    def __move_on_top(self, key: str, value: str):
        try:
            self.__delitem__(key)
        except KeyError:
            pass
        self.__setitem__(key, value)
        if len(self) > self.capacity:
            self.popitem()
        return value
