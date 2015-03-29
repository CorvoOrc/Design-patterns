__author__ = 'Corvo'


class Duck(object):

    def __init__(self, fly_behavior, quack_behavior):
        self.fly_behavior = fly_behavior
        self.quack_behavior = quack_behavior

    def swim(self):
        pass

    def display(self):
        pass

    def perform_fly(self):
        self.fly_behavior.fly()

    def perform_quack(self):
        self.quack_behavior.quack()

    def set_fly_behavior(self, behavior):
        self.fly_behavior = behavior

    def set_quack_behavior(self, behavior):
        self.quack_behavior = behavior


class FlyBehavior(object):

    def __init__(self):
        pass

    def fly(self):
        raise NotImplementedError


class QuackBehavior(object):

    def __init__(self):
        pass

    def quack(self):
        raise NotImplementedError


class FlyWithWings(FlyBehavior):

    def fly(self):
        print 'I`m flying!'


class FlyNoWay(FlyBehavior):

    def fly(self):
        print 'I can`t fly'


class Quack(QuackBehavior):

    def quack(self):
        print 'quack quack'


class Squick(QuackBehavior):

    def quack(self):
        print 'wuuii'


class MallardDuck(Duck):

    def __init__(self, fly_behavior, quack_behavior):
        super(MallardDuck, self).__init__(fly_behavior, quack_behavior)

    def display(self):
        print 'MallardDuck'


class RubberDuck(Duck):

    def __init__(self, fly_behavior, quack_behavior):
        super(RubberDuck, self).__init__(fly_behavior, quack_behavior)

    def display(self):
        print 'RubberDuck'


mallard = MallardDuck(FlyWithWings(), Quack())
mallard.perform_fly()
mallard.perform_quack()
mallard.set_fly_behavior(FlyNoWay())
mallard.set_quack_behavior(Squick())
mallard.perform_fly()
mallard.perform_quack()
