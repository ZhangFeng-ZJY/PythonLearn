fruitd = {'西瓜': 20, '葡萄': 20, '香蕉': 13, '苹果': 21 }
fruitd1 = {'西瓜': '南京', '葡萄': '北京', '香蕉': '海南', '苹果': '山西'}

df = dict(zip(fruitd.values(), fruitd.keys()))

for fruitd, fruitd1 in df.items():
    print(f"{fruitd}在{fruitd1}是{df[fruitd]}")