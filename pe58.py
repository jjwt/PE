def isprime(n):
	if n<=1:
		return False
	t=n
	for i in range(2,int(t**0.5)+1):
		if t%i==0:
			return False
	return True
def gen(i):
	if i==0:
		return [1]
	if i>=1:
		return [(2*i+1)**2-2*i*j for j in range(4)]
	pass
tall=0
i=1
while 1:
	t=gen(i)
	#print t
	for j in t:
		if isprime(j):
			tall+=1
	m=1.0*tall/(4*i+1)
	#print m,
	if m<0.1:
		print 2*i+1
		break
	i+=1
