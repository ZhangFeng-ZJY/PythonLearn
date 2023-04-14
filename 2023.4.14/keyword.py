import keyword

s = str(input())

s1 = " ".join(keyword.kwlist)

def isia(s):
	for i in range(0, 9):
		if s[0] == i:
			return True
	return False

if isia(s1) or s1.find(s):
	print("不能作为标识符")
else:
	print("可以")

