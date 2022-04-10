from z3 import *

# solution
x = Real("x")
y = Real("y")
z = Real("z")

# Prove Properties here
#Addition commutes
prove((x + y == y + x))
#Addition is associative
prove((x + y) + z == x + (y + z))
prove(Or(x < 0, x > 0, x == 0))
prove(x*x >= 0)

x = FP("x", Float16())
y = FP("y", Float16())
z = FP("z", Float16())

prove((x + y == y + x))
#Addition is associative
prove((x + y) + z == x + (y + z))
prove(Or(x < 0, x > 0, x == 0))
prove(x*x >= 0)

# FILL IN
