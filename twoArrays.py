def solve(x,y,n):
    i=0;j=0;c=0
    while(i<len(x)):
        while(j<len(y)):
            #print i,j
            if(int(x[i])+int(y[j])>=int(n[1])):
                print x.pop(i),y.pop(j)
                print x,y
                i=0
                j=0
                c=1
            else:
                j=j+1
                c=0
                print x,y
        if(c==0):
            i=i+1
    if(len(x)==0):
        print "YES"
    else:
        print "NO"
for i in range (0,input()):
    n=raw_input().split()
    x=raw_input().split()
    y=raw_input().split()
    solve(x,y,n)
