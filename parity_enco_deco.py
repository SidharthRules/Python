def pari(x):
	cnt = 0
	for i in x:
		#print i
		if i=='1':
			cnt+=1
	#print cnt
	return cnt%2;

# The Encoder Logic
x=raw_input('Dataword: ')
x+=str(pari(x))
print 'Codeword:',x

# The Decoder Logic
x=raw_input('Codeword: ')
