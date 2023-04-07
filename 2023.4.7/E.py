'''
n1 = 1
n2z = x
n2m = 1

n2z = n2z * x
n2m = n2m * (n2m+1)
'''

x = int(input('请输入X:'))

s = 0

s = s + 1
nz = x
nm = 1
while nz / nm > 1e-6:
	s = s + nz / nm
	nz = nz * x
	nm = nm * (nm + 1)
print(s)
