mas=[]
for x in '0123456789abcdefghijklmnopqrs':
    y = int(f'923{x}874',29)+int(f'524{x}6152',29)
    if y%28==0:
        mas.append(x)
print(max(mas))
R=int('923r874',29)+int('524r6152',29)
print(R/28)