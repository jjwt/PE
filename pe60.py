#from itertools import combinations as com
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

def isprime(n):
	if n<=1:
		return False
	t=n
	for i in range(2,int(t**0.5)+1):
		if t%i==0:
			return False
	return True

########################################################################

N=makeprime(100000)
N.remove(2)
N.remove(5)

########################################################################

def isit1(x,y):
	t=int(str(x)+str(y))
	if not isprime(t):
		return False
	t=int(str(y)+str(x))
	if not isprime(t):
		return False
	return True

########################################################################

def isit(n,lis):
	for i in lis:
		if not isit1(n,i):
			return False
	return True

########################################################################

def main():
	an=[[N[i]] for i in range(10)]
	ans=an[:]
	for i in range(10,len(N)):
		for j in ans:
			if isit(N[i],j):
				#print j,
				if len(j)==1:
					ans.append([j[0],N[i]])
				else:
					j.append(N[i])
				#print j
				if len(j)==5:
					print j,sum(j)
					quit()
				#print ans

########################################################################

main()
