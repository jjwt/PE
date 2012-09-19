def isprime(n):
	for i in range(2,int(n**0.5)+1):
		if n%i==0:
			return False
	return True

########################################################################

def isit(x,y):
	t1=[i for i in str(x)]
	t1.sort()
	t2=[i for i in str(y)]
	t2.sort()
	return t1==t2

########################################################################

def main():
	n=10**7
	t=int(n**0.5)
	man=range(2,2*t)
	tlis=[i for i in man if isprime(i)]
	an=n
	for i in range(len(tlis)):
		for j in range(i+1,len(tlis)):
			t=tlis[i]*tlis[j]
			if t<n:
				m=(tlis[i]-1)*(tlis[j]-1)
				if isit(m,t):
					tt=1.0*t/((tlis[i]-1)*(tlis[j]-1))
					if tt<an:
						an=tt
						print tlis[i],tlis[j],t,tt

########################################################################

main()
