from z3 import *

x, y, x1, y1, temp = Ints("x y x1 y1 temp")

twosort = [ If(y < x, And(temp == x, x1 == y, y1 == temp), And(x1 == x, y1 == y)) ] 

prove( Implies(And(twosort), x1 <= y1))
