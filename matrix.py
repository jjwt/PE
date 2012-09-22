def isreal(n):
	return type(n)==int or type(n)==float
def ismatrix(lis):
	if not type(lis)==list:
		return False
	m=len(lis)
	if m==0:
		return False
	if not type(lis[0])==list:
		return False
	n=len(lis[0])
	for i in range(1,m):
		if n != len(lis[i]):
			return False
		for j in lis[i]:
			if not isreal(j):
				return False
	return True
def matrix_check_ismatrix(*matrixs):
	for matrix in matrixs:
		if not ismatrix(matrix):
			raise "the argument should be a matrix!"
def matrix_add(A,B):
	matrix_check_ismatrix(A,B)
	m=len(A)
	n=len(A[0])
	if m!=len(B) or n!=len(B[0]):
		raise "the two matrix should be of the same struct!"
	C=[range(n) for i in range(m)]
	for i in range(m):
		for j in range(m):
			C[i][j]=A[i][j]+B[i][j]
	return C
def matrix_scalar_mult(n,A):
	if not ismatrix(A):
		raise "matrix_scalar_mult(n,A), the argument A should be a matrix"
	if not isreal(n):
		raise "matrix_scalar_mult(n,A), the argument n should be an int or a float"
	m=len(A)
	n=len(A[0])
	C=[range(n) for i in range(m)]
	for i in range(m):
		for j in range(n):
			C[i][j]=n*A[i][j]
	return C
def matrix_subtraction(A,B):
	return matrix_add(A,matrix_scalar_mult(-1,B))
def matrix_mult(A,B):
	matrix_check_ismatrix(A,B)
	s=len(A[0])
	if s!=len(B):
		raise  "the two arguments should be inner-size same!"
	m=len(A)
	n=len(B[0])
	C=[range(n) for i in range(m)]
	for i in range(m):
		for j in range(n):
			C[i][j]=sum([A[i][k]*B[k][j] for k in range(s)])
	return C
def matrix_print(A):
	matrix_check_ismatrix(A)
	for i in A:
		for j in i:
			print j,'\t',
		print
def test():
	a=[[1,2,-1],\
			[3,4,0],\
			[-2,5,6]]
	b=[[10,20],\
			[-10,30],\
			[-5,8]]
	#matrix_print(matrix_mult(a,b))
	matrix_print(matrix_mult(b,a))
test()
