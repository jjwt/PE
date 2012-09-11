from itertools import combinations as com
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

def isprime(n):
	if n<=1:
		return False
	t=n
	for i in range(2,int(t**0.5)+1):
		if t%i==0:
			return False
	return True
a=makeprime(10000)
print len(a)
def isit(n):
	t=com(list(n),2)
	while 1:
		try:
			t1,t2=t.next()
		except StopIteration:
			break
		tt1=int(str(t1)+str(t2))
		tt2=int(str(t2)+str(t1))
		if not isprime(tt1):
			return False
		if not isprime(tt2):
			return False
	return True
def gen2():
	ta=com(a,5)
	while 1:
		t=ta.next()
		if isit(t):
			print t,
			print sum(t)
			break

def gen1():
	nlen=len(a)
	for i1 in range(nlen):
		for i2 in range(i1+1,nlen):
			for i3 in range(i2+1,nlen):
				for i4 in range(i3+1,nlen):
					for i5 in range(i4+1,nlen):
						t=[a[i] for i in [i1,i2,i3,i4,i5]]
						if isit(t):
							print t,
							print sum(t)
							break

gen1()
