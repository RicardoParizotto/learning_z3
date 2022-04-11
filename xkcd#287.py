from z3 import *

a, b, c, d, e, f = Ints("a b c d e f")
s = Solver()

s.add(a*2.15 + b*2.75 + c*3.35 + d*3.55 + e*4.20 + f*5.80 == 15.05)
s.add(a >= 0)
s.add(b >= 0)
s.add(c >= 0)
s.add(d >= 0)
s.add(e >= 0)
s.add(f >= 0)

print (s.check())
print (s.model())
