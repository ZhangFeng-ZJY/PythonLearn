## 三角

a, b, c = map(int, input().split())
if a + b + c > 2 * max(a, b, c):
	s = (a + b + c) / 2
	area = (s * (s - a) * (s - b) * (s - c)) ** 0.5
	print('三角形面积为 %0.2f' % area)
else:
    print("不能构成三角形")

