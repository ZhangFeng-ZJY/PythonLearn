#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @author : liuhefei
# @desc: 互质勾股数
for i in range(1, 101):
	a = i
	# 输入的a为奇数，则a = 2n+1，b=2n**2+2n，c=2n**2+2n+1
	if a >= 3 and a % 2 == 1:
		n = (a - 1) // 2
		b = 2 * n**2 + 2*n
		c = 2 * n**2 + 2*n + 1
		if a <= 100 and b <= 100 and c <= 100:
			print(a, b, c, sep = ',', end = '\n')
	else:
		# 输入的a为偶数，则a = 2n，b=n**2-1，c=n**2+1
		if a >= 3 and a % 2 == 0:
			n = a // 2
			b = n**2 - 1
			c = n**2 + 1
			if a <= 100 and b <= 100 and c <= 100:
				print(a, b, c, sep = ',', end = '\n')

