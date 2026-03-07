
def zadacha_append(zadacha):
   if zadacha !='':
        list_zadach.append([str(len(list_zadach)+ 1), zadacha])
        print('задача добавлена')
   else:
       print('вы ввели пустую задачу')
def zadacha_remove(zadacha):
    list_zadach.remove(zadacha)
def list_clear():
   proverka = input('вы уверены, если да введите 1')
   if proverka == '1':
       list_zadach.clear()
   else:
       print('всё осталось')
def all_zadach():
    for zad in list_zadach:
        print(' '.join(zad))

list_zadach =[]
while True:
    print('1: посмотреть задачи')
    print('2: добавить задачу')
    print('3: удалить задачу')
    print('4: очистить список')
    change = input('введите номер опции')
    if change == '1':
        all_zadach()
    if change == '2':
        zadacha = input('введите задачу')
        zadacha_append(zadacha)
    if change == '3':
        zadacha = input('введите задачу')
        zadacha_remove(zadacha)
    if change == '4':
        list_clear()
