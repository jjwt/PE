def fact(n):
	t=1
	for i in range(1,n+1):
		t*=i
	return t
def gen1(n):
	return sum([fact(int(i)) for i in str(n)])
def gen2(n):
	t=set([n,])
	tt=n
	while 1:
		tt=gen1(tt)
		if not tt in t:
			t.add(tt)
		else:
			break
	return len(t)
print gen2(1000000)
N=1000000
an=0
for i in range(1,N):
	if gen2(i)==60:
		an+=1
print an
