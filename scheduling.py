from z3 import *



# RAM , storage , both in GB
messages =[(2 , 7) ,
(7, 10) , (10,13),
(8, 12) ,
(13, 14) ,
(13, 19)]


set_len =len(messages)

s= Optimize()
#s.set(priority='pareto')
rt =[]

vars =[ Int('vars_ %d' % i) for i in range ( set_len )]


for i in range ( set_len ):
	rt.append(vars[i]* (messages[i][1] - messages[i][0]))
	s.add(Or(vars[i]==0 , vars[i]==1) ) # like bools


s.add([Implies(And(vars[i]==1, vars[j]==1), Or(Or(messages[i][1] <= messages[j][0], messages[j][1] <= messages[i][0]), i == j)) for i in range(set_len) for j in range(set_len)]) 

s.maximize(sum(rt))
#s.maximize(sum(vars))
#s.add(sum(vars) >=1) 

if s. check () == unsat :
	print(s)
	print ("unsat ")
	exit (0)
m=s.model()
print(m)

for i in range ( set_len ):
	if m[vars[i]]. as_long () ==1:
		print (messages[i],)
