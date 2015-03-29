__author__ = 'Corvo'


class Subject(object):

    def register_observer(self, observer):
        raise NotImplementedError

    def remove_observer(self, observer):
        raise NotImplementedError

    def notify_observer(self):
        raise NotImplementedError


class Observer(object):

    def update(self):
        raise NotImplementedError


class DisplayElement(object):

    def display(self):
        raise NotImplementedError


class WeatherData(Subject):

    def __init__(self):
        self.listeners = []
        self.temperature = 0
        self.humidity = 0

    def register_observer(self, observer):
        self.listeners.append(observer)

    def remove_observer(self, observer):
        self.listeners.remove(observer)

    def notify_observer(self):
        for o in self.listeners:
            o.update()

    def set_fields(self, temperature, humidity):
        self.temperature = temperature
        self.humidity = humidity
        self.notify_observer()


class CurrentConditionsDisplay(Observer):

    def __init__(self, subject):
        self.subject = subject
        subject.register_observer(self)
        self.temperature = 1
        self.humidity = 1

    def update(self):
        self.temperature = self.subject.temperature
        self.humidity = self.subject.humidity
        self.display()

    def display(self):
        print 'temperature:{temperature}, humidity:{humidity}'.format(temperature=self.temperature, humidity=self.humidity)


weather_data = WeatherData()
current_display = CurrentConditionsDisplay(weather_data)
weather_data.set_fields(temperature=12, humidity=7564)
weather_data.set_fields(temperature=-22, humidity=7453)
