sum = 0
for i in range(1, 1001):
	if i % 3 == 0:
		if (i % 10) / 6 == 1:
			sum = sum + i
print(sum)
