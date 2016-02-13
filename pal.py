def isPal(s):
    for i in xrange(len(s)//2):
        if s[i] != s[len(s)-i-1]:
            return False
    return True
 
def solve(s):
    for i in xrange((len(s)+1)//2):
        if s[i] != s[len(s)-i-1]:
            if isPal(s[:i]+s[i+1:]):
                return i
            else:
                return len(s)-i-1
    return -1
for i in range(0,input()):
    x=raw_input()
    print solve(x)
