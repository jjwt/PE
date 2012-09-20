def test(n):
	t=n
	while 1:
		m=3*t-1
		if m%7==0:
			print m/7,t
			break
		t-=1
test(1000000)
