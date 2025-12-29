mas=[]
for x in'0123456789abcdefghi':
    y= int(f'11H{x}05',18)+int(f'3F{x}54{x}8',18)+int(f'G{x}{x}{x}9',18)
    if y%14==0:
        mas.append(x)
print(mas)
# r=int(f'12h734',18)+int(f'8h95h3',18)+int(f'24h796',18)
# print(r/14)