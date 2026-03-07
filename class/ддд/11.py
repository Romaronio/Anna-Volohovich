mas=[]
for x in range(1,55):
    for y in range(1,55):
        k=0
        z=5**50+5**30-5**x-y-5**y-x
        while z>0:
            if z%5==0:
                k+=1
            z=z//5
        if k==10:
            mas.append(x*y)
print(mas,k)