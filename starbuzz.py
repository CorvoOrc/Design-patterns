__author__ = 'Corvo'


class Beverage(object):

    def __init__(self):
        self._description = None

    @property
    def description(self):
        return self._description

    @property
    def cost(self):
        raise NotImplementedError


class Espresso(Beverage):

    def __init__(self):
        self._description = 'Espresso'

    @property
    def cost(self):
        return 1.99


class DarkRoast(Beverage):

    def __init__(self):
        self._description = 'DarkRoast'

    @property
    def cost(self):
        return .99


class HouseBlend(Beverage):

    def __init__(self):
        self._description = 'HouseBlend'

    @property
    def cost(self):
        return .59


class CondimentDecorator(Beverage):

    def __init__(self):
        pass

    @property
    def description(self):
        raise NotImplementedError

    @property
    def cost(self):
        raise NotImplementedError


class Mocha(CondimentDecorator):

    def __init__(self, beverage):
        self.beverage = beverage
        self._description = 'Mocha'

    @property
    def description(self):
        return self.beverage.description + ' ' + self._description + ' '

    @property
    def cost(self):
        return self.beverage.cost + .20


class Milk(CondimentDecorator):

    def __init__(self, beverage):
        self.beverage = beverage
        self._description = 'Milk'

    @property
    def description(self):
        return self.beverage.description + ' ' + self._description + ' '

    @property
    def cost(self):
        return self.beverage.cost + .30


class Whip(CondimentDecorator):

    def __init__(self, beverage):
        self.beverage = beverage
        self._description = 'Whip'

    @property
    def description(self):
        return self.beverage.description + ' ' + self._description + ' '

    @property
    def cost(self):
        return self.beverage.cost + .05


beverage = Espresso()
print '{description} ${cost}'.format(description=beverage.description, cost=beverage.cost)
beverage1 = DarkRoast()
beverage1 = Mocha(beverage1)
beverage1 = Mocha(beverage1)
beverage1 = Milk(beverage1)
print '{description} ${cost}'.format(description=beverage1.description, cost=beverage1.cost)
