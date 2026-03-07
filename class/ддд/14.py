k=[]
slovo = 'окорок'
for i in slovo:
    kol_vo = slovo.count(i)
    k.append([kol_vo, i])
print(max(k))
