from collections import deque

def str_Red(x):
    q = deque([x])
    ml = len(x)
    while q:
        x = q.popleft()
        if len(x) < ml:
            ml = len(x)
        for i in xrange(len(x)-1):
            substring = x[i:(i+2)]
            if substring == "ab" or substring == "ba":
                q.append(x[:i] + "c" + x[(i+2):])
            elif substring == "bc" or substring == "cb":
                q.append(x[:i] + "a" + x[(i+2):])
            elif substring == "ac" or substring == "ca":
                q.append(x[:i] + "b" + x[(i+2):])
    return ml

for i in range(0,input()):
	x=raw_input()
	print str_Red(x)
