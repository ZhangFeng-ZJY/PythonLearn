def fun(num):
    i = 0
    while num > 0:
        digit = num % 10
        num = num // 10
        i = i + 1

    n = 0
    while num > 0:
        digit = num % 10
        list[n] = digit
        num = num // 10
        n = n + 1

fun(123)