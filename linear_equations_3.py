from z3 import *

x, y = Reals('x y')
s = Solver()
s.add(x >= 0)
s.add(Or(x + y <= 2, x + 2*y >= 6))
s.add(Or(x + y >= 2, x + 2*y > 4))

print (s.check())
print (s.model())
