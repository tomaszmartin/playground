class Test:
    pass

test_type = type(Test)
assert test_type == type
# That's kind of weird
assert type(type) == type


# Other way to define a class
bases = ()
attr = {}
Foo = type('Foo', bases, attr)
assert type(Foo()) == Foo


# Sample metaclass for building 
# Singleton objects
class SingletonMeta(type):
    _instances = {}
    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(SingletonMeta, cls).__call__(*args, **kwargs)
        return cls._instances[cls]

class Singleton(metaclass=SingletonMeta):
    pass

assert Singleton() == Singleton()

# What if we have attributes?
class AttrSingleton(metaclass=SingletonMeta):
    def __init__(self, x):
        self.x = x

# They seem the same
assert AttrSingleton(1) == AttrSingleton(2)
inst1 = AttrSingleton(1)
inst2 = AttrSingleton(2)
assert inst1.x == inst2.x
# Be carefull with this!
assert inst1.x == 1
assert inst2.x == 1
# If we delete those we still can't 
# build inst with different value
del inst1
del inst2
inst3 = AttrSingleton(3)
assert inst3.x == 1


# Try using weakref
from weakref import WeakKeyDictionary
class WeakrefSingletonMeta(type):
    _instances = WeakKeyDictionary()
    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(WeakrefSingletonMeta, cls).__call__(*args, **kwargs)
        return cls._instances[cls]

class WeakSingleton(metaclass=WeakrefSingletonMeta):
    def __init__(self, x):
        self.x = x

inst1 = WeakSingleton(1)
assert inst1.x == 1
del inst1
inst2 = WeakSingleton(2)
# Still no luch in redefinig it
assert inst2.x == 1
# But it is still there
assert WeakSingleton._instances[WeakSingleton].x == 1
