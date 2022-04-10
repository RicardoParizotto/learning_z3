from z3 import *

digits = Ints('s e n d m o r y')
s,e,n,d,m,o,r,y = digits


send = Sum([10**(3-i) * d for i,d in enumerate([s,e,n,d])])
more = Sum([10**(3-i) * d for i,d in enumerate([m,o,r,e])])
money = Sum([10**(4-i) * d for i,d in enumerate([m,o,n,e,y])])

solver = Solver()

solver.add([s > 0, m > 0])

solver.add([And(d >= 0, d <=9) for d in digits])
solver.add([Distinct(digits)])
solver.add(send + more == money)

print(solver.check())
print(solver.model())
