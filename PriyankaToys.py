def calc(x):
	#lim=x[0]
	cnt=1
	for i in range(0,len(x)):
		if(x[i]>(x[0]+4)):
			cnt=cnt+1
	print cnt
input()
x=map(int,raw_input().split())
calc(x)
