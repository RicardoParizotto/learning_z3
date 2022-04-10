from z3 import *

x, y = Reals('x y')
solve([y==0, y == x**3 + 3*x**2 + 4*x + 2])
