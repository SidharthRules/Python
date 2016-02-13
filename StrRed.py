def cnt(x):
	m={}
	m['a']=0;m['b']=0;m['c']=0
	for c in x:
		if c not in m:
			m[c]=1
		else:
			m[c]+=1
	return m
def red(x):
	xm=cnt(x)
	print x,xm
	if((xm['a']==0 and xm['b']==0 ) or (xm['a']==0 and xm['c']==0 ) or (xm['b']==0 and xm['c']==0)):
		return len(x);
	if((xm['a']%2==0 and xm['b']%2==0 and xm['c']%2==0) or (xm['a']%2==1 and xm['b']%2==1 and xm['c']%2==1)):
		return 2
	return 1
for i in range(0,input()):
	x=raw_input()
	#print x
	print red(x)
