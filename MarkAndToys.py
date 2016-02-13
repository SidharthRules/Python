def toyFinder(x,y):
    cnt=0
    i=x[0]-1
    y.sort()
   # print x[1],y
    while(i>-1):
		if(x[1]>y[i]):
			x[1]-=y[i]
			cnt+=1
		else:
			y.pop(i)
		i-=1
    #print x[1],cnt,y
    return cnt         
        
rs=map(int,raw_input().split())
ty=map(int,raw_input().split())
print toyFinder(rs,ty)
