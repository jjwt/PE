def gen(n):
	i=1
	while 1:
		a=1+i**2*n
		if a==(int(a**0.5))**2:
			return str(a**0.5),n
		i+=1
an={}
for i in range(1,1000+1):
	print i
	if i!=(int(i**0.5))**2:
		c,d=gen(i)
		if an.has_key(c):
			an[c].append(d)
		else:
			an[c]=[d]
a=max(an.keys())
print an[a]
