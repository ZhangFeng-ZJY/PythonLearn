season = int(input('请输入是几月:'))

if season in (12, 1, 2):
	print('冬季')
elif season in (3, 4, 5):
	print('春季')
elif season in (6, 7, 8):
	print('夏季')
elif season in (9, 10, 11):
	print('秋季')
else:
	print('您输入的月份不合法!')
