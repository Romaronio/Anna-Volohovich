# slovo= 'abc'
# if 'ab' in slovo:
#     print('ok')

flag=1
parol='1234'
user_parol= input('введите пароль')
for i in user_parol:
    if i in parol:
        flag=1
    else:
        flag=0
        break
if flag==1:
    print('ok')
else:
    print('not ok')