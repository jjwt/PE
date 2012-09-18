from itertools import permutations
ta1=range(1,11)
p1=permutations(ta1,3)
an=[]
def gen(t):
	tt=t[:]
	a=min([i[0] for i in tt])
	while tt[0][0]!=a:
		tt=[tt[-1]]+tt[:-1]
	return tt
while 1:
	try:
		t1=p1.next()
	except:
		break
	ta2=[i for i in ta1 if i not in t1]
	p2=permutations(ta2,2)
	while 1:
		try:
			t2=p2.next()
		except:
			break
		if sum(t2)==sum(t1[:-1]):
			t2=(t2[0],t1[-1],t2[1])
			ta3=[i for i in ta1 if i not in t2+t1]
			p3=permutations(ta3,2)
			while 1:
				try:
					t3=p3.next()
				except:
					break
				if sum(t3)==sum(t2[:-1]):
					t3=(t3[0],t2[-1],t3[1])
					ta4=[i for i in ta1 if i not in t3+t2+t1]
					p4=permutations(ta4,2)
					while 1:
						try:
							t4=p4.next()
						except:
							break
						if sum(t4)==sum(t3[:-1]):
							t4=(t4[0],t3[-1],t4[1])
							t5=[i for i in ta1 if i not in t4+t3+t2+t1][0]
							t5=(t5,t4[-1],t1[1])
							if sum(t4)==sum(t5):
								t=[t1,t2,t3,t4,t5]
								t=gen(t)
								if not t in an:
									print sum(t1),t
									an.append(t)

t=0
for i in an:
	tt=int(''.join([str(j) for j in i[0]+i[1]+i[2]+i[3]+i[4]]))
	print tt
	if len(str(tt))==16 and tt>t:
		t=tt
print t
