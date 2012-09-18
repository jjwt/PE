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

########################################################################

def Euler_totient(n,lis):
	t=n
	an=1
	for i in lis:
		while t%i==0:
			t=t/i
			if t%i==0:
				an=an*(i)
			else:
				an=an*(i-1)
		if t==1:
			break
	return an

########################################################################

def main():
	tan,an=0,0
	allprimes=makeprime(10**6)
	for i in range(1,10**6+1):
		t=1.0*i/Euler_totient(i,allprimes)
		if tan<t:
			tan,an=t,i
	print an,tan

def test(n):
	for i in range(1,n):
		print i,Euler_totient(i,makeprime(n))

########################################################################

main()
