n=input()
b=input()
ex=n%b
x=[0]*b;
for i in range(b):
	x[i]=n/b;
i=0
while(ex>0):
	x[i]+=1
	ex-=1
	i+=1

print x
