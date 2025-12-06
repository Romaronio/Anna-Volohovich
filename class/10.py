mas=[]
for x in'0123456789abcdefghijklmn':
    y= int(f'12{x}734',24)+int(f'8{x}95{x}3',24)+int(f'24{x}796',24)
    if y%23==0:
        mas.append(x)
print(mas)
r=int(f'12h734',24)+int(f'8h95h3',24)+int(f'24h796',24)
print(r/23)