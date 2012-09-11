def isit(x,y,d):
	return x**2-d*y**2==1
def gcd(x,y):
	while y:
		x,y=y,x%y
	return x
def issquare(n):
	return n==(int(n**0.5))**2
def gen1(mlist):
	a,b=1,mlist[-1]
	for t in mlist[:-1][::-1]:
		a,b=b,t*b+a
	a,b=b,a
	t=gcd(a,b)
	a,b=a/t,b/t
	return a,b
def gen(n):
	mlist=[]
	a,b=0,1
	t=0
	for i in range(1000):
		m=int((n**0.5+a)/b)
		mlist.append(m)
		a,b=m*b-a,(n-(a-m*b)**2)/b
		#print m,gen1(mlist)
		x,y=gen1(mlist)
		if len(str(x))>len(str(y)):
			t+=1
	print t

gen(2)
