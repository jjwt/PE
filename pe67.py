def fetch():
	f=open('triangle.txt','r')
	data=[]
	for line in f.readlines():
		data.append([int(i) for i in line.split()])
	return data

########################################################################

def main():
	a=fetch()
	for n in range(len(a)-2,-1,-1):
		for j in range(len(a[n])):
			a[n][j] += a[n+1][j+(a[n+1][j]<=a[n+1][j+1])]
	print a[0][0]

########################################################################

main()
