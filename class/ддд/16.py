k=0
kol_vo_bukv=0
parol='1234'
user_parol=input('введите пароль')
kol_vo_parol = len(parol)
for i in parol:
    if user_parol[k] == i:
        kol_vo_bukv+=1
    k+=1
if kol_vo_parol == kol_vo_bukv:
    print('ок'
        )
elif kol_vo_parol-1==kol_vo_bukv:
    print('ок')
else:
    print('нет')

