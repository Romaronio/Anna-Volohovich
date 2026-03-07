mas = []
k =0
for x in range(0,3000):
    y = 9*11**210+8*11**150-x
    while y>0:
        if y%11==0:
            k=k+1
        y=y//11
        print(k)
    if k == 60:

        mas.append([k,x])
res = max(mas)
print(res)