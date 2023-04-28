## 三个整数

a, b ,c = map(int, input().split())

if a > b :
	if b > c:
		print(a, b, c)
	elif a > c:
		print(a, c, b)
	else:
		print(c, a, b)
elif a > c:
	print(b, a, c)
elif b > c:
	print(c, b, a)
else:
	print(c, b, a)
