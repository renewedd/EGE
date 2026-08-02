def hello(name):
    print("hello", name)

n = 'Den'
hello(n)
hello("Nickolay")
hello("Sofiya")

def s(a,b):
    return a*b
square = s(2,3)
print(square)

def s (r, pi = 3.14):
    return 2 * pi * r, pi * r * 2

p,s = s(2, 3)
print(p)
print(s)

import math
print(math.floor(5.5))
print(math.ceil(5.2))

from math import floor, ceil
print(floor(5.5))
print(ceil(5.2))

from math import *
print(floor(5.5))
print(ceil(5.2))
