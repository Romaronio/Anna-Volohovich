N = int(input('введите количество дней:'))
summ = 0
k = 0
for i in range(N):
    a = int(input('введите температуру:'))
    if a > 0:
        summ += a
        k += 1
print(summ/k)
print(k)