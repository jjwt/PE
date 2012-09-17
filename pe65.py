def gcd(x,y):
	while y:
		x,y=y,x%y
	return x

########################################################################

def gen1(mlist):
	a,b=1,mlist[-1]
	for t in mlist[:-1][::-1]:
		a,b=b,t*b+a
	a,b=b,a
	t=gcd(a,b)
	a,b=a/t,b/t
	return a,b

########################################################################

def main():
	tt=range(100)
	tt[0]=2
	for i in range(1,len(tt)):
		if i%3==2:
			tt[i]=2*(i+1)/3
		else:
			tt[i]=1
	t=gen1(tt)
	print sum([int(i) for i in str(t[0])])

########################################################################

main()
