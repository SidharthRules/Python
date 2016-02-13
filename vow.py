v={'a':0,'e':0,'i':0,'o':0,'u':0,}
k={'b':0,'c':0,'d':0,'f':0,'g':0,'h':0,'j':0,'k':0,'l':0,
'm':0,'n':0,'p':0,'q':0,'r':0,'s':0,'t':0,'v':0,'w':0,
'x':0,'y':0,'a':0,}
def cle(x):
	for i in x:
		if x[i]!=0:
			print i,':',x[i],' ',
	print
x=raw_input()
for i in x:
	#print "This is :",i
	if i in v:
		v[i]+=1
	elif i in k:
		k[i]+=1
print 'Vowels: ',
cle(v)
print 'Consonants: ',
cle(k)
