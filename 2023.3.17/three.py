a, b, c = map(int, input('请输入三个整数:').split())
maxn = a if a > b else b
maxn = c if c > maxn else maxn
print(maxn)
