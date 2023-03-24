month, day = map(int, input("请输入月份与日期:(用空格隔开)").split())

if month == 1:
	if day >= 1 and day <= 19:
		print("摩羯座")
	else:
		print("水瓶座")
elif month == 2:
	if day >= 1 and day <= 18:
		print("水瓶座")
	else:
		print("双鱼座")
elif month == 3:
	if day >= 1 and day <= 21:
		print("双鱼座")
	else:
		print("白羊座")
elif month == 4:
	if day >= 1 and day <= 19:
		print("白羊座")
	else:
		print("金牛座")
elif month == 5:
	if day >= 1 and day <= 20:
		print("金牛座")
	else:
		print("双子座")
elif month == 6:
	if day >= 1 and day <= 21:
		print("双子座")
	else:
		print("巨蟹座")
elif month == 7:
	if day >= 1 and day <= 22:
		print("巨蟹座")
	else:
		print("狮子座")
elif month == 8:
	if day >= 1 and day <= 22:
		print("狮子座")
	else:
		print("处女座")
elif month == 9:
	if day >= 1 and day <= 22:
		print("处女座")
	else:
		print("天秤座")
elif month == 10:
	if day >= 1 and day <= 23:
		print("天秤座")
	else:
		print("天蝎座")
elif month == 11:
	if day >= 1 and day <= 22:
		print("天蝎座")
	else:
		print("射手座")
elif month == 12:
	if day >= 1 and day <= 21:
		print("射手座")
	else:
		print("摩羯座")
