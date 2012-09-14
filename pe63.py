def gen(n):
	a=0
	for i in range(1,10):
		t=i**n
		if len(str(t))==n:
			print n,t,i
			a+=1
	return a

########################################################################

def main():
	an=0
	for i in range(1,100):
		an+=gen(i)
	print an

########################################################################

main()
