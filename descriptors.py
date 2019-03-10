# 1. How instance methods work?
class Test:
    """Testing how descriptors work."""

    def __init__(self, attr=None):
        self.attr = attr

    def ret(self):
        return self
    
    # What's wrong here?
    def show(msg):
        print(msg)

# Depending on how we call the show method
# we pass it the instance or not
# The line below works
Test.show('Wrong definition works ok on class?')
# but this one is not 
# since it implicitly passes self
try:
    Test().show('And on instance?')
except TypeError:
    print('But not on the instance.')

# Due to descriptor the signature of
# the method changes dynamically
instance = Test()
assert Test.ret.__get__(instance, Test) == instance.ret
assert Test.ret.__get__(instance, Test)() == instance

# Descriptors work onluy on the class level?
# Since these gives the same results
returned = Test.ret.__get__(instance, Test)()
assert returned == instance
# But this do not
assert not Test().ret.__get__(instance, Test)() == instance
# Altough this works fine :P
type(Test()).ret.__get__(instance, Test)() == instance
print()


# 2. Staticmethod implementation in Python
class StaticMethod:
    "Emulate PyStaticMethod_Type() in Objects/funcobject.c"

    def __init__(self, f):
        self.f = f

    def __get__(self, obj, objtype=None):
        return self.f

class StaticMethodTest:

    @StaticMethod
    def test(arg):
        return arg

assert StaticMethodTest.test(1) == StaticMethodTest().test(1)

# What if we try to use it on regular function?
@StaticMethod
def regular_func(arg):
    print(arg)

try:
    regular_func(1)
except TypeError:
    print('Actually it doesn\'t work. Functions don\'t use descriptors.')
print()


# 3. Classmethod implementation in Python
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

class ClassMethodTest:
    
    @ClassMethod
    def test(cls, arg):
        return arg

assert ClassMethodTest.test(1) == ClassMethodTest().test(1)
print()


# 4. Just for fun, implmentation of InstanceMethod
# This way it would be less ambigous
# than the current implementation
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

class InstanceMethodTest:

    @InstanceMethod
    def test(self, arg):
        self.arg = arg
        return arg

try:
    InstanceMethodTest.test()
except TypeError:
    print('Can\'t invoke instance method from class')
print()


# 5. How about properties?
# Can You control setting property value?
class NonNullProperty:

    def __init__(self, initval=0):
        self.val = initval
    
    def __set__(self, obj, value):
        if not value:
            raise AttributeError('You shall not pass!')
        self.val = value

class NonNullPropertyTest:
    x = NonNullProperty()

# On instance
try:
    # This should not work
    NonNullPropertyTest().x = None
except AttributeError:
    print('Cannot set NonNullProperty to None on instance!')
else:
    print('I did set NonNullProperty to None on instance!')

# And on class
try:
    # But this works just fine
    NonNullPropertyTest.x = None
except AttributeError:
    print('Cannot set NonNullProperty to None on class!')
else:
    print('I did set NonNullProperty to None on class! It is no longer NonNullProperty either...')

NonNullPropertyTest().x = None
print('And now it\'s no problem to set it to None...')

# How can You control getting property value
class InvisibleProperty:

    def __init__(self, initval=0):
        self.val = initval
    
    def __get__(self, obj, objtype=None):
        raise AttributeError('Can\'t see me!')
    
    def __set__(self, obj, value):
        self.val = value

class InvisiblePropertyTest:
    x = InvisibleProperty()

# On instance
try:
    # This should not work
    print(InvisiblePropertyTest().x)
except AttributeError:
    print('I really can\'t see the InvisibleProperty!')

# On class
try:
    # Neither do this
    print(InvisiblePropertyTest.x)
except AttributeError:
    print('Even from the class!')


# What happens if we cahnge class atrribute 
# On the instance level?
class ClassAttr:
    x = 1

i1 = ClassAttr()
i2 = ClassAttr()
assert i1.x == i2.x
i1.x = 2
# It changes the value
assert i1.x == 2
# But only for a given instance
assert i2.x == 1


# What happens with read only property?
class ClassProperty:
    @property
    def x(self):
        return 1

i1 = ClassProperty()
i2 = ClassProperty()
# This indeed raises and error
try:
    i1.x = 10
except AttributeError:
    print('Read only attributes work on instance level!')

try:
    ClassProperty.x = 2
    print('But You can do what You want on class level!')
except AttributeError:
    pass


# To sum up:
# - descriptors work for methods on both class and instance level
#   but if You invoke them on class level
# - but on attributes not so much
#   when set from class level they are overriden like any other value
#   no magic here, but getting works as expected
