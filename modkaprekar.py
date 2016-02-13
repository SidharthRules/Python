def sendKap(x,s):
	y=x*x
	y=str(y)
	s1=y[:len(y)/2:]
	s2=y[len(y)/2::]
	s3=int(s1)+int(s2)
	if(s3==x):
		s.append(str(x))
st=input()
en=input()
s=[]
for i in range(st,en+1):
	if(i>9):
		sendKap(i,s)
	elif(i==1):
		s.append(str(i))
	elif(i==9):
		s.append(str(i))
if(len(s)==0):
	print 'INVALID RANGE'
else:
	print ' '.join(s)
