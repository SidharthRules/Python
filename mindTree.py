z=[]
for i in range(1,input()+1):
	z.append(i)
x=[]
a=b=0
i=1
while(b<len(z)):
	a=b
	b=b+i
	s=z[a:b]
	if(i%2!=0):
		print s
	else:
		print s[::-1]
	i+=1
