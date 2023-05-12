import random

my_list = [random.randint(1, 10) for _ in range(100)]

# 定义一个字典，用于统计每个数字在列表中出现的次数
digit_count = {}

# 遍历列表中的每个数字，并将其添加到字典中
for num in my_list:
    digit_count[num] = digit_count.get(num, 0) + 1

# 输出字典中的每个键值对
for digit, count in digit_count.items():
    print(f"{digit}: {count}")