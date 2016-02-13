c=0
x=[[0,0,0],[0,0,0],[0,0,0]]
y=[[1,2,3],[4,5,6],[7,8,9]]
def fin(x,y):
	d1=d2=0
	c1=c2=c3=0
	r1=r2=r3=0
	for i in range(0,3):
		for j in range(0,3):
			if(i==j and x[i][j]==y):
				d1+=1
			if(i+j==2 and x[i][j]==y):
				d2+=1
			if(i==0 and x[i][j]==y):
				r1+=1
			if(i==1 and x[i][j]==y):
				r2+=1
			if(i==2 and x[i][j]==y):
				r3+=1
			if(j==0 and x[i][j]==y):
				c1+=1
			if(j==1 and x[i][j]==y):
				c2+=1
			if(j==2 and x[i][j]==y):
				c3+=1	
	if(c1==3 or c2==3 or c3==3 or d1==3 or d2==3 or r1==3 or r2==3 or r3==3 ):
		return True
	else:
		return False
def pri(x,y):
	print '  Game\t','\tStructure'
	for i in range(3):
		print x[i],'\t',y[i]
def chk(x,p):
	if(fin(x,p)==True):
		print 'Player',p,'wins!'
		c=1
def stor(x,inp,pl):
	if(inp==1):
		x[0][0]=pl
	elif(inp==2):
		x[0][1]=pl
	elif(inp==3):
		x[0][2]=pl
	elif(inp==4):
		x[1][0]=pl
	elif(inp==5):
		x[1][1]=pl
	elif(inp==6):
		x[1][2]=pl
	elif(inp==7):
		x[2][0]=pl
	elif(inp==8):
		x[2][1]=pl
	elif(inp==9):
		x[2][2]=pl

while(True):
	pri(x,y)
	print 'Player 1: Enter Pos 1'
	p1=input()
	stor(x,p1,1)
	chk(x,1)
	if(c==1):
		break;
	pri(x,y)
	print 'Player 2: Enter Pos 2'
	p2=input()
	stor(x,p2,2)
	chk(x,2)
	if(c==1):
		break;
	
