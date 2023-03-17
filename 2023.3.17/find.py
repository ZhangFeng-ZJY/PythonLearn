a, b, c = map(int, input('请输入三个球a,b,c的质量:').split())
if (a == b and a != c):
	print('c球不同')
elif (a == c and a != b):
	print('b球不同')
elif (b == c and b != a):
	print('a球不同')
