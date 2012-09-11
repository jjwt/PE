from itertools import repeat as p
Ewords=range(65,91)+range(97,123)+[ord(i) for i in ",.; \t0123456789()'!"]
#print [chr(i) for i in Ewords]
#keys=[ord(i) for i in 'god']
f=open('cipher1.txt','r')
words=[int(i) for i in f.read().split(',')]
#print words
def isit(key):
	i=0
	rc=words
	for j in range(len(rc)):
		rc[j]=rc[j]^key[i]
		if not rc[j] in Ewords:
			#print rc[j]
			return False,rc
		i+=1
		if i==3:
			i=0
	return True,rc
keys=range(97,123)
def main():
	for k1 in keys:
		for k2 in keys:
			for k3 in keys:
				key=[k1,k2,k3]
				if key==[ord(i) for i in 'god']:
					print key
				c,d=isit(key)
				#if key==[ord(i) for i in 'god']:
					#print c,d
				if c:
					print [chr(i) for i in d]
def test():
	key=[ord(i) for i in 'god']
	c,d=isit(key)
	if c:
		#print [chr(i) for i in d if i not in Ewords]
		print [chr(i) for i in d]
		#print d
main()
