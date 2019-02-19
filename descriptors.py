class Test:
    """Testing how descriptors work."""

    def __init__(self, attr=None):
        self.attr = attr

    def ret(self):
        return self
    
    # What's wrong here?
    def show(msg):
        print(msg)

# Depending on how we call show we pass it the instance or not
# The line below works
Test.show('What the Fuck?')
# but this one is not (since it implicitly passes self)
try:
    Test().show('What the Fuck?')
except TypeError:
    print('What the Fuck?')

# Due to descriptor the signature of
# the method changes dynamically
instance = Test()
assert Test.ret.__get__(instance, Test) == instance.ret
assert Test.ret.__get__(instance, Test)() == instance

# But only on the class level?
# Since these gives the same results
returned = Test.ret.__get__(instance, Test)()
assert returned == instance
# But this is not
assert not Test().ret.__get__(instance, Test)() == instance
# Altough this works :P
type(Test()).ret.__get__(instance, Test)() == instance


# Staticmethod implementation in Python
class StaticMethod:
    "Emulate PyStaticMethod_Type() in Objects/funcobject.c"

    def __init__(self, f):
        self.f = f

    def __get__(self, obj, objtype=None):
        return self.f

class Sample:

    @StaticMethod
    def test(arg):
        return arg

assert Sample.test(1) == Sample().test(1)

# What if we try to use it on regular function?
@StaticMethod
def regular_func(arg):
    print(arg)

try:
    regular_func(1)
except TypeError:
    print('Actually it doesn\'t work. Functions don\'t use descriptors.')


# Classmethod implementation in Python
class ClassMethod:
    "Emulate PyClassMethod_Type() in Objects/funcobject.c"

    def __init__(self, f):
        self.f = f

    def __get__(self, obj, objtype=None):
        if objtype is None:
            objtype = type(object)
        def func(*args):
            return self.f(objtype, *args)
        return func

class Sample:
    
    @ClassMethod
    def test(cls, arg):
        return arg

assert Sample.test(1) == Sample().test(1)


# Just for fun, implmentation of InstanceMethod
# This way it would be less ambigous
# than current implementation
class InstanceMethod:
    "Emulate PyClassMethod_Type() in Objects/funcobject.c"

    def __init__(self, f):
        self.f = f

    def __get__(self, obj, objtype=None):
        def func(*args):
            if obj is None:
                msg = f'{self.f.__name__}() has to be invoked from an instance'
                raise TypeError(msg)
            return self.f(obj, *args)
        return func

class Sample:

    @InstanceMethod
    def test(self, arg):
        self.arg = arg
        return arg

try:
    Sample.test()
except TypeError:
    print('Can\'t invoke instance method from class')


# How about properties?
class NonNullProperty:

    def __init__(self, initval=0):
        self.val = initval
    
    def __set__(self, obj, value):
        if not value:
            raise ValueError('You shall not pass!')
        self.val = value
    
    def __repr__(self):
        return repr(self.val)

class Test:
    x = NonNullProperty()

test = Test()
try:
    test.x = None
except ValueError:
    print('Seems legit!')

# What if I try to access it?
test.x = 1
print('Set NonNullProperty to', test.x)
