__author__ = 'Corvo'


class EventCategory(object):

    def __init__(self):
        pass


class Event(object):
    callers = {}

    def __init__(self, default_category=None):
        self._default_cat = default_category

    def attach(self, event_category, handler):
        if event_category is None:
            event_category = self._default_cat
        self.callers.setdefault(event_category, [])
        self.callers[event_category].append(handler)
        return self

    def dettach(self, event_category, handler=None):
        if event_category is None:
            event_category = self._default_cat
        if handler is not None:
            del self.callers[event_category][handler]
        else:
            del self.callers[event_category]
        return self

    def __call__(self, *args, **kwargs):
        category = kwargs['category']
        if category in self.callers:
            del kwargs['category']
            for handler in self.callers[category]:
                handler(*args, **kwargs)

    def __iadd__(self, handler):
        return self.attach(None, handler)

    def __isub__(self, handler):
        return self.detach(None, handler)
