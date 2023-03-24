season = int(input('请输入是几月:'))

if season in (12, 1, 2):
	print('冬季')
elif season <= 5:
	print('春季')
elif season <= 8:
	print('夏季')
elif season <= 11:
	print('秋季')
else:
	print('您输入的月份不合法!')
