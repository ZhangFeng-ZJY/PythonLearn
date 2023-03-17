side1, side2, side3 = map(int, input('请输入三角形的三边:').split())
if ((side1 + side2 > side3) | (side2 + side3 > side1) | (side1 + side3 > side2)):
	print('可以组成三角形!')
else:
	print('不可以!')
