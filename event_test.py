__author__ = 'Corvo'

from event_caller import EventCategory, Event

def print_callback_event():
    print '_callback'

def print_yet_callback_event():
    print '_callback'

def append_callback_event(list, item):
    list.append(item)


print_cat = EventCategory()
add_cat = EventCategory()
event = Event(print_cat)

event.attach(print_cat, print_callback_event)
event.attach(print_cat, print_yet_callback_event)
event += print_callback_event
event(category=print_cat)

event.attach(add_cat, append_callback_event)
items = [1, 2, 3, 7]
event(category=add_cat, list=items, item=2)
print items
