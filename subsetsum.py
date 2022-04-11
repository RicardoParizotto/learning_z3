from z3 import *

set =[-7, -3, -2, 5, 8]
set_len =len(set)

vars =[ Int('vars_ %d' % i) for i in range ( set_len )]

s= Solver ()
rt =[]
for i in range ( set_len ):
	rt. append (vars[i]* set[i])
	s.add(Or(vars[i]==0 , vars[i]==1) ) # like bools
# rt here is [ vars_0 *-7, vars_1 *-3, vars_2 *-2, vars_3 *5, vars_4 *8]
s.add(sum(rt)==0)

s.add(sum(vars) >=1) # subset must not be empty
if s. check () == unsat :
	print ("unsat ")
	exit (0)
m=s.model()

for i in range ( set_len ):
	if m[vars[i]]. as_long () ==1:
		print (set[i],)
