def jisu(n):
    fl = 1
    for i in range(1, n + 1):
        fl = fl * (fl + 2)
    return fl

def func(n):
    s=1
	while(n):
		s*=n
		n-=1
	return s

pai = 1
while number / 1000000 > 1e-6:
    flag = 1
    pai = pai + 