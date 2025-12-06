mas=[]
for x in '0123456789abcdefghijklmnopqrs':
    y = int(f'463{x}7921',29)+int(f'8241{x}153',29)
    if y%28==0:
        mas.append(x)
print(max(mas))
r=int('463s7921',29)+int('8241s153',29)
print(r/28)