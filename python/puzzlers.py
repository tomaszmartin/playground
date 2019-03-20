class Test:

    def __init__(self, arg=None):
        self.arg = arg

# Seems that Python resues id (addresses) where it can
# Works when used as python3 module.py
# but doesn't work on Jupyter
oldid = id(Test())
newid = id(Test())
assert oldid == newid

# The same if we initiate it with the same argument
oldid = id(Test(1))
newid = id(Test(1))
assert oldid == newid

# And even with different one
oldid = id(Test(1))
newid = id(Test(1))
assert oldid == newid

# Default classes are passed as reference
# Same as lists unlike int or floata
def func(atest):
    atest.arg = 1

test = Test()
assert test.arg is None
func(test)
assert test.arg == 1
