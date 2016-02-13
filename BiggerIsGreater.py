from itertools import permutations
def BIG(x):
	y=[''.join(p) for p in permutations(x)]
	return map(str,set(y))[map(str,set(y)).index(x)-1]
for i in range(0, input()):
	x=raw_input()
	print BIG(x)
