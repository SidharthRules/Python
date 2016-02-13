from itertools import chain, combinations

def powerset(x):
    s = list(x)
    print s
    return chain.from_iterable(combinations(s, r) for r in range(len(s)+1))

def twotwo(t):
	k=[]
	for i in range(20):
		k.append(2**i)
	t.pop(0)
	#return len(set(k).intersection(set(map(int,t))))
	#print [filter(lambda x: x in t, sublist) for sublist in k]
	#print [val for val in k if str(val) in t]
	x=[]
	t= map(int,set(map(int,t)))
	for i in t:
		if int(i) in k:
			x.append(int(i))
	print x

for i in range(input()):
	x=raw_input()
	#cnt=len(map(int,str(x)))-len(set(map(int,str(x))))
	cnt=0
	t=list(map(''.join, powerset(x)))
	twotwo(t)
