__author__ = 'Corvo'


class Singleton(object):

    def __init__(self, decorated):
        self._decorated = decorated

    def instance(self):
        try:
            return self._instance
        except AttributeError:
            self._instance = self._decorated()
            return self._instance

    def __call__(self):
        raise TypeError('Singletons must be accessed through `instance()`.')

    def __instancecheck__(self, inst):
        return isinstance(inst, self._decorated)


@Singleton
class ChocolateBoiler(object):

    def __init__(self):
        self._is_empty = True
        self._is_boiled = False

    def fill(self):
        if self._is_empty:
            self._is_empty = False
            self._is_boiled = False


try:
    chocolate_boiler = ChocolateBoiler()
except Exception as e:
    print e.message
instance1 = ChocolateBoiler.instance()
instance2 = ChocolateBoiler.instance()
print instance1 == instance2
