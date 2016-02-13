#Program to find all the possible permutaions of a number
x=input()
for i in range(2**len(str(x))-1):
	print i,'combination'
