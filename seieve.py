t=input()
x=[1]*t
x[0]=0;
x[1]=0;
print x
for i in range(2,int(pow(t,0.5))+1):
	print 'IN Loop'
	if(x[i]==1): 
		k=i*i;
		j=0
		while((i*j+k)<t):
			print 'In LOOP'
			x[(i*j)+k]=0;
			j=j+1;
print x
