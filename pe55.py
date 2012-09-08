def ispalindromic(n):
	return str(n)==str(n)[::-1]

def isit(n):
	a=n
	for i in range(50):
		a=int(str(a)[::-1])+a
		if ispalindromic(a):
			return False
	return True
t=0
for i in range(1,10**4):
	if isit(i):
		t+=1
print t
