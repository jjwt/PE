#coding:utf-8
from time import time
#main1来自网友xw_y_am，main2是我在此基础上改进的，时间减少了一半左右
def main1():
	gcd=lambda x,y:y==0 and x or gcd(y,x%y)
	N=1500000
	lmax=int(((2*N+1)**0.5-1)/2)
	an=[]
	for m in range(1,lmax+1):
		#print m
		for n in range(1,m):
			t=[2*m*n,m**2-n**2,m**2+n**2]
			if gcd(t[0],t[1])==1:
				an.append(sum(t))
	out,delete=set(),set()
	for i in an:
		t=i
		while t<=N:
			if t in out:
				out.remove(t)
				delete.add(t)
			else:
				if not t in delete:
					out.add(t)
			t+=i
	print len(out)
def main2():
	gcd_ori = lambda x, y: y == 0 and x or gcd_ori(y, x % y)

	def gcd(lis):
	  out = lis[0]
	  for i in lis:
		out = gcd_ori(out, i)
	  return out

	def calc(i, j):
	  return (i ** 2 - j ** 2, 2 * i * j, i ** 2 + j ** 2)

	def make(x):
	  out = []
	  for i in xrange(2, int(x ** 0.5)):
		for j in xrange(1, i):
		  c = calc(i, j)
		  if gcd(c) == 1:
			out.append(sum(c))
	  return out
	  

	maxx = 1500000
	unit = make(maxx)
	out = set([])
	delete = set([])
	for i in unit:
	  n = 1
	  while 1:
		tmp = i * n
		if tmp > maxx:
		  break
		if tmp in out:
		  out.remove(tmp)
		  delete.add(tmp)
		else:
		  if not tmp in delete:
			out.add(tmp)
		n += 1


	print len(out)

t1=time()
main1()
print time()-t1
t1=time()
main2()
print time()-t1
