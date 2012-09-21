def makeprime(x):
	p=[2]
	P=[2]
	n=3
	while n<x:
		for i in p:
			if n % i ==0:
				break
		else:
			P.append(n)
		while n > p[-1]**2:
			p.append(P[len(p)])
		n+=2
	return P
#print len(allprimes)
def gen(n,lis):
	t=n
	an=1
	for i in lis:
		if t in lis:
			an=an*(t-1)
			return an
		else:
			while 1:
				if t%i==0:
					if t/i%i==0:
						an=an*i
						t=t/i
					else:
						an=an*(i-1)
						t=t/i
				if t%i!=0:
					break
		if t==1:
			return an
def main(n):
	t=0
	allprimes=makeprime(n)
	for i in range(2,n+1):
		t+=gen(i,allprimes)
		print i
	print t
main(10**6)
