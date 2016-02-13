#!/usr/bin/py
# Head ends here
def stringReduction(a):
    z=[]
    i=0
    while(i<len(a)-1):
		sb=a[i:i+2]
		if(sb=='bc' or sb=='cb'):
			a=a[:i]+'a'+a[(i+2):]
			i=0
		elif(sb=='ab' or sb =='ba'):
			a=a[:i]+'c'+a[(i+2):]
			i=0
		elif(sb=='ac' or sb=='ca'):
			a=a[:i]+'b'+a[(i+2):]
			i=0
		else:
			i+=1	
         
    return len(a)
for i in range(0,input()):
	x=raw_input()
	#print x
	print stringReduction(x)
