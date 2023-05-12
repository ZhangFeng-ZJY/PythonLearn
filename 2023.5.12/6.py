def square(a, b, c):
    if a + b > a and a + c > b and b + c > a:
        p = (a + b + c) / 2
        S = (p * (p - a) * (p - b) * (p - c)) ** 0.5
        return S
    return "三边不合理"

a = int(input('第一边:'))
b = int(input('第三边:'))
c = int(input('第二边:'))


print(square(a, b, c))