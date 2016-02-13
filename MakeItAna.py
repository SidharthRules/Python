def gen(x):
	m={}
	for c in x:
		if c not in m:
			m[c]=1
		else:
			m[c]+=1
	return m
def chk(x,y):
	xm=gen(x)
	ym=gen(y)
	print xm,ym
	cnt=0
	for i in ym.keys():
		if i not in xm:
			cnt+=ym[i]
		else:
			cnt+= max(0, ym[i]-xm[i])
	for i in xm.keys():
		if i not in ym:
			cnt+=xm[i]
		else:
			cnt += max(0, xm[i]-ym[i])
	print cnt
x=raw_input();
y=raw_input();
print x,y
chk(x,y)
