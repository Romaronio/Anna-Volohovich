# from operator import *
# mas = [int(i) for i in open('10.txt')]
# sum = 0
# res = []
# for i in range(len(mas) - 1):
# 	if xor(mas[i] % 80 == 17, mas[i + 1] % 80 == 17):
# 		if mas[i] % 7 == 0 and mas[i + 1] % 7 == 0:
# 			res.append(mas[i] + mas[i + 1])
# for i in res:
# 	if i % 80 == 17:
# 		sum += i
# print(len(res), sum)

# f = open("10.txt")
# a = [int(i) for i in f]
# k = 0
# sum_el_17 = 0
# for i in range(len(a) - 1):
#     if ((a[i] % 80 == 17) + (a[i + 1] % 80 == 17)) == 1:
#         if a[i] % 7 == 0 and a[i + 1] % 7 == 0:
#             k += 1
#             sum_el_17 += a[i] if a[i] % 80 == 17 else a[i + 1]
# print(k,sum_el_17)


mas = [int(i) for i in open('10.txt')]
res = []
for i in range(len(mas) - 1):
	if mas[i] % 3 == 0 or mas[i + 1] % 3 == 0:
		res.append(mas[i] + mas[i + 1])
print(len(res), max(res))


