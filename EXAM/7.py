import re

sttr = input("请输入一个字符串")
print(re.sub('\D', '', sttr))

s = ''.join([x for x in sttr if x.isalpha()])
print(s)

