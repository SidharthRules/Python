t=input()
x=[0]*t
z=[0]*t
for i in range(t):
	y=map(int,raw_input().split())
	x[i]=y[0]+y[1]
	z[i]=y[0]+y[1]
z.sort()
#print x,z
for i in range(t):
	print x.index(z[i])+1,
