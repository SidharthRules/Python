#deepak ka pass ex cl !!
print 'Enter the list of elements followed by space:'
x=raw_input();
x=map(int,x.split())
for i in range(0, len(x)-1):
 for j in range(0,len(x)-i-1):
  if(x[j]>x[j+1]):
   swp=x[j]
   x[j]=x[j+1]
   x[j+1]=swp
print x

# dProbuk @ http://www.dprobuk.com/2015/09/bubble-sort-in-python.html#ixzz3lZzkOdjS
