mas = []
k = 0
for x in range(0,7290):
    y = 27 ** 298+ 27** 269 -x
    while y>0:
        if y % 27 == 0:
            k +=1
        y = y // 27
        mas.append([k,x])
res = max(mas)
print(res)
