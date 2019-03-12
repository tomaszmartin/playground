import ctypes
import sys

# CPython looks up values for small integers
# in a small_ints array
# This way values from small ints (-5, 256) ale always the same
# i.e. have the same address

i = 256
assert i is 256

# Throws an error when run from terminal
i = 257
assert i is 257

# TODO: Not sure why the values for dst, src and count
def mutate_int(an_int, new_value):
    ctypes.memmove(id(an_int) + 24, id(new_value) + 24, 8)

mutate_int(256, 512)
print(256)
mutate_int(1, 10)
print(1)