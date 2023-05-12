def fun(num):
    list = []
    while num > 0:
        digit = num % 10
        list.append(digit)
        num = num // 10
    sum = 0
    for i in range(0, len(list)):
        sum = sum + list[i]
    print(sum)

fun(123)
