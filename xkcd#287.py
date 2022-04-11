from z3 import *

#https://sat-smt.codes/SAT_SMT_by_example.pdf
#https://www.xkcd.com/287/

appetizers = Ints("a b c d e f")
a, b, c, d, e, f = appetizers
s = Solver()

s.add(a*2.15 + b*2.75 + c*3.35 + d*3.55 + e*4.20 + f*5.80 == 15.05)
s.add([And(d >= 0) for d in appetizers]) 
print (s.check())
print (s.model())
