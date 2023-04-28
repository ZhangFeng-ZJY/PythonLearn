
b = []
for i in range(2, 100):
    for a in range(2, i-1):
        if i % a == 0:
            break
    else:
        b.append(i)


for x in range(2,len(b)):
    if b[x] - b[x-1] ==2:
        print(b[x-1],b[x])
