from z3 import *

p, q = Bools('p q')


#De Morgan's Law
prove(And(p, q) == Not(Or(Not(p), Not(q))))
prove(Implies(p, q) == Or(Not(p), q))
#Peirce's Law
prove(Implies(Implies(Implies(p, q), p), p))
