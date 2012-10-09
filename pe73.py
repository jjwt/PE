def quyu(x,y):
	while y:
		x,y=y,x%y
	return x

def main():
	N=12000
	an=0
	for i in range(2,N/2):
		if i%2==0:
			t=2*i+1
			while t<3*i and t<=N:
				if quyu(t,i)==1:
					an+=1
				t+=2
		else:
			t=2*i+1
			while t<3*i and t<=N:
				if quyu(t,i)==1:
					an+=1
				t+=1
	print an
main()
