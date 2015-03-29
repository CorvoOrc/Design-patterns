__author__ = 'Corvo'


class PizzaStore(object):

    def __init__(self):
        pass

    def orderPizza(self, type):
        pizza = self.create_pizza(type)

        pizza.prepare()
        pizza.bake()
        pizza.cut()
        pizza.box()

        print 'PizzaStore->orderPizza'

        return pizza

    def create_pizza(self, type):
        raise NotImplementedError


class NYStylePizzaStore(PizzaStore):

    def __init__(self):
        print 'NYStylePizzaStore->create'

    def create_pizza(self, type):
        print 'NYStylePizzaStore->create_pizza'
        igredient_factory = NYPizzaIngredientFactory()

        if type == NYStyleCheesePizza:
            return NYStyleCheesePizza(igredient_factory)
        elif type == NYStylePepperoniPizza:
            return NYStylePepperoniPizza(igredient_factory)
        else:
            return None


class ChicagoStylePizzaStore(PizzaStore):

    def __init__(self):
        print 'ChicagoStylePizzaStore->create'

    def create_pizza(self, type):
        print 'ChicagoStylePizzaStore->create_pizza'
        igredient_factory = ChicagoPizzaIngredientFactory()

        if type == ChicagoStyleCheesePizza:
            return ChicagoStyleCheesePizza(igredient_factory)
        elif type == ChicagoStylePepperoniPizza:
            return ChicagoStylePepperoniPizza(igredient_factory)
        else:
            return None


class Pizza(object):

    def __init__(self):
        self.name = "Corvo Pizza!"
        self.cheese = None
        self.pepperoni = None

    def prepare(self):
        raise NotImplementedError

    def bake(self):
        print 'Pizza->bake'

    def cut(self):
        print 'Pizza->cut'

    def box(self):
        print 'Pizza->box'


class Cheese(object):

    def __init__(self):
        print 'Cheese->create'


class Pepperoni(object):

    def __init__(self):
        print 'Pepperoni->create'


class ReggianoCheese(Cheese):

    def __init__(self):
        print 'ReggianoCheese->create'


class MozarellaCheese(Cheese):

    def __init__(self):
        print 'MozarellaCheese->create'


class SlicedPepperoni(object):

    def __init__(self):
        print 'SlicesPepperoni->create'


class PiePepperoni(object):

    def __init__(self):
        print 'PiePepperoni->create'


class PizzaIngredientFactory(object):

    def __init__(self):
        pass

    def create_cheese(self):
        raise NotImplementedError

    def create_pepperoni(self):
        raise NotImplementedError


class NYPizzaIngredientFactory(PizzaIngredientFactory):

    def __init__(self):
        print 'NYPizzaIngredientFactory->create'

    def create_cheese(self):
        return ReggianoCheese()

    def create_pepperoni(self):
        return SlicedPepperoni()


class ChicagoPizzaIngredientFactory(PizzaIngredientFactory):

    def __init__(self):
        print 'ChicagoPizzaIngredientFactory->create'

    def create_cheese(self):
        return MozarellaCheese()

    def create_pepperoni(self):
        return PiePepperoni()


class NYStyleCheesePizza(Pizza):

    def __init__(self, ingredient_factory):
        self.ingredient_factory = ingredient_factory

    def prepare(self):
        self.cheese = self.ingredient_factory.create_cheese()
        self.pepperoni = self.ingredient_factory.create_pepperoni()

    def bake(self):
        print 'CheesePizza->bake'

    def cut(self):
        print 'CheesePizza->cut'

    def box(self):
        print 'CheesePizza->box'


class ChicagoStyleCheesePizza(Pizza):

    def __init__(self, ingredient_factory):
        self.ingredient_factory = ingredient_factory

    def prepare(self):
        self.cheese = self.ingredient_factory.create_cheese()
        self.pepperoni = self.ingredient_factory.create_pepperoni()

    def bake(self):
        print 'CheesePizza->bake'

    def cut(self):
        print 'CheesePizza->cut'

    def box(self):
        print 'CheesePizza->box'


class NYStylePepperoniPizza(Pizza):

    def __init__(self, ingredient_factory):
        self.ingredient_factory = ingredient_factory

    def prepare(self):
        self.cheese = self.ingredient_factory.create_cheese()
        self.pepperoni = self.ingredient_factory.create_pepperoni()

    def bake(self):
        print 'PepperoniPizza->bake'

    def cut(self):
        print 'PepperoniPizza->cut'

    def box(self):
        print 'PepperoniPizza->box'


class ChicagoStylePepperoniPizza(Pizza):

    def __init__(self, ingredient_factory):
        self.ingredient_factory = ingredient_factory

    def prepare(self):
        self.cheese = self.ingredient_factory.create_cheese()
        self.pepperoni = self.ingredient_factory.create_pepperoni()

    def bake(self):
        print 'PepperoniPizza->bake'

    def cut(self):
        print 'PepperoniPizza->cut'

    def box(self):
        print 'PepperoniPizza->box'


pizza_store = ChicagoStylePizzaStore()
pizza = pizza_store.orderPizza(ChicagoStyleCheesePizza)
print pizza
