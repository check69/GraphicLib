from typing import Union

class BasicClass(object):
    def __init__(self):
        self._x = True

    @property
    def x(self) -> Union[str, int, bool, list, dict]:
        return self._x


class ChildClass(BasicClass):
    def __init__(self):
        super(ChildClass, self).__init__()
        self._x = 5

class OtherClass(object):
    def __init__(self, o1: BasicClass):
        if not isinstance(o1, BasicClass):
            raise TypeError("o1 must be a BasicClass")

        self._object = o1

    def get_object(self) -> BasicClass:
        return self._object
