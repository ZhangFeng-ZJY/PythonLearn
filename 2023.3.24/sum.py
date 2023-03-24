n = int(input("请输入一个正整数:"))
sum = 0
if n % 2 == 0:
	for i in range(2, n + 1, 2):
		sum = sum + i
elif n % 2 == 1:
	for i in range(2, n, 2):
		sum = sum + i
print(sum)
