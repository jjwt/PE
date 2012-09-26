#coding:utf-8
from copy import deepcopy
def isreal(n):
	#判断是否为实数
	return type(n)==int or type(n)==float
def ismatrix(lis):
	#判断是否二维表
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
			raise TypeError, "the argument should be a matrix!"
def matrix_add(A,B):
	matrix_check_ismatrix(A,B)
	m=len(A)
	n=len(A[0])
	if m!=len(B) or n!=len(B[0]):
		raise TypeError, "the two matrix should be of the same struct!"
	C=[range(n) for i in range(m)]
	for i in range(m):
		for j in range(m):
			C[i][j]=A[i][j]+B[i][j]
	return C
def matrix_scalar_mult(n,A):
	#矩阵的数乘
	if not ismatrix(A):
		raise TypeError, "matrix_scalar_mult(n,A), the argument A should be a matrix"
	if not isreal(n):
		raise TypeError, "matrix_scalar_mult(n,A), the argument n should be an int or a float"
	m=len(A)
	n=len(A[0])
	C=[range(n) for i in range(m)]
	for i in range(m):
		for j in range(n):
			C[i][j]=n*A[i][j]
	return C
def matrix_subtraction(A,B):
	#矩阵的减法
	return matrix_add(A,matrix_scalar_mult(-1,B))
def matrix_mult(A,B):
	matrix_check_ismatrix(A,B)
	s=len(A[0])
	if s!=len(B):
		raise  TypeError, "the two arguments should be inner-size same!"
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
def matrix_transpose(A):
	#矩阵的转置
	matrix_check_ismatrix(A)
	m=len(A)
	n=len(A[0])
	C=[range(m) for i in range(n)]
	for i in range(n):
		for j in range(m):
			C[i][j]=A[j][i]
	return C
def matrix_is_phalanx(A):
	#判断是否方阵
	matrix_check_ismatrix(A)
	m=len(A)
	n=len(A[0])
	return m==n
def matrix_is_antisymmetric(A):
	#判断是否反对称矩阵
	matrix_check_ismatrix(A)
	if not matrix_is_phalanx(A):
		raise TypeError,"Should be a phalanx matrix!"
	return A==matrix_scalar_mult(-1,matrix_transpose(A))
def matrix_is_symmetric(A):
	#判断是否对称矩阵
	matrix_check_ismatrix(A)
	if not matrix_is_phalanx(A):
		raise TypeError,"Should be a phalanx matrix!"
	return A==matrix_transpose(A)
def matrix_determinant(A,precision=1e-6):
	#计算行列式的值
	if not matrix_is_phalanx(A):
		raise TypeError,"Should be a phalanx matrix!"
	n=len(A[0])
	C=deepcopy(A)
	an=1.0
	for i in range(n-1):
		if abs(C[i][i])<precision:
			for j in range(i+1,n):
				if abs(C[j][i])>precision:
					C[i],C[j]=C[j],C[i]
					an*=-1
					break
		if abs(C[i][i])<precision:
			return 0.0
		for j in range(i+1,n):
			t=-1.0*(C[j][i])/C[i][i]
			for k in range(n):
				C[j][k]+=t*C[i][k]
	if abs(C[-1][-1])<precision:
		return 0.0
	for i in range(n):
		an*=C[i][i]
	return an
def matrix_gen_E(n):
	#生成n阶单位阵
	C=[[0.0]*n for i in range(n)]
	#matrix_print(C)
	for i in range(n):
		C[i][i]=1
	return C
def matrix_inverse(A,precision=1e-6):
	#初等变换法计算矩阵的逆
	if abs(matrix_determinant(A))<=precision:
		raise InputError,"the determinant value of matrix should not be zero!"
	B=deepcopy(A)
	n=len(A)
	C=matrix_gen_E(n)
	#matrix_print(C)
	for i in range(n-1):
		if abs(C[i][i])<precision:
			for j in range(i+1,n):
				if abs(C[j][i])>precision:
					B[i],B[j]=B[j],B[i]
					C[i],C[j]=C[j],C[i]
					break
		for j in range(i+1,n):
			t=-1.0*(B[j][i])/B[i][i]
			for k in range(n):
				B[j][k]+=t*B[i][k]
				C[j][k]+=t*C[i][k]
	for i in range(n-1,0,-1):
		for j in range(i-1,-1,-1):
			t=-1.0*(B[j][i])/B[i][i]
			for k in range(n):
				B[j][k]+=t*B[i][k]
				C[j][k]+=t*C[i][k]
	for i in range(n):
		t=B[i][i]
		for j in range(n):
			B[i][j]/=t
			C[i][j]/=t
	return B,C
def test():
	a=[[1,2,3],
			[2,2,1],
			[3,4,3]]
	for i in matrix_inverse(a):
		matrix_print(i)
test()
