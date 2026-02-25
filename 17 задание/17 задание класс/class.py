# f = open(r'C:\Users\spiri\Desktop\егэ материалы\17 задание\17 задание класс\1.txt')
# res = []
# for s in f:
# 	chislo = int(s)
# 	if chislo % 3 == 0 and chislo % 7 != 0 and chislo % 17 != 0 and chislo % 19 != 0 and chislo % 27 != 0:
# 		res.append(chislo)
# print(len(res), max(res))


# f = open(r'C:\Users\spiri\Desktop\егэ материалы\17 задание\17 задание класс\2.txt')
# res = []
# for s in f:
# 	chislo = int(s)
# 	if chislo % 10 == 5 or chislo % 10 == 7:
# 		if chislo % 9 != 0 and chislo % 11 != 0:
# 			res.append(chislo)

# print(len(res), max(res) + min(res))


# mas = [int(i) for i in open(r'C:\Users\spiri\Desktop\егэ материалы\17 задание\17 задание класс\3.txt')]
# res = []
# for i in mas:
# 	if i % 16 == 11 and i % 7 == 0 and i % 6 != 0 and i % 13 != 0 and i % 19 != 0:
# 		res.append(i)
# print(sum(res), len(res))


# mas = [int(i) for i in open(r'C:\Users\spiri\Desktop\егэ материалы\17 задание\17 задание класс\4.txt')]
# res = []
# for i in range(len(mas) - 1):
# 	if (mas[i] + mas[i + 1]) % 3 == 0 and (mas[i] + mas[i + 1]) % 6 != 0:
# 		if str((mas[i] * mas[i + 1]))[-1] == '8':
# 			res.append(mas[i] + mas[i+1])
# print(len(res), max(res))


# f = open(r'C:\Users\spiri\Desktop\егэ материалы\17 задание\17 задание класс\5.txt')
# mas = []
# for s in f:
# 	ch = int(s)
# 	mas.append(ch)
# res = []
# for i in range(len(mas) - 1):
# 	if (mas[i] * mas[i + 1]) > 0:
# 		if (mas[i] + mas[i + 1]) % 7 == 0:
# 			res.append(mas[i] * mas[i + 1])
# print(len(res), min(res))


# mas = [int(i) for i in open(r'C:\Users\spiri\Desktop\егэ материалы\17 задание\17 задание класс\6.txt')]

# k = 0
# for i in mas:
# 	if i % 5 == 0:
# 		k += 1
# res = []
# for i in range(len(mas) - 1):
# 	if (mas[i] < 0 and mas[i + 1] > 0) or (mas[i] > 0 and mas[i + 1] < 0):
# 		if (mas[i] + mas[i + 1]) < k:
# 			res.append(mas[i] + mas[i + 1])

# print(len(res), max(res))


# mas = [int(i) for i in open(r'C:\Users\spiri\Desktop\егэ материалы\17 задание\17 задание класс\7.txt')]
# k = 0
# for s in mas:
# 	if s % 3 == 0:
# 		k += 1
# kol = len([i for i in mas if i % 3 == 0])
# res = []
# for i in range(len(mas) - 1):
# 	if mas[i] < 0 or mas[i + 1] < 0:
# 		if (mas[i] + mas[i + 1]) < kol:
# 			res.append(mas[i] + mas[i + 1])
# print(len(res), max(res))


# from operator import *
# f = open(r'C:\Users\spiri\Desktop\егэ материалы\17 задание\17 задание класс\8.txt')
# mas = []
# for s in f:
# 	mas.append(int(s))

# kol = [i for i in mas if abs(i) % 10 == 9]
# res = []
# for i in range(len(mas) - 1):
# 	if xor(abs(mas[i]) % 10 == 9, abs(mas[i + 1]) % 10 == 9):
# 	# if (mas[i] % 10 == 9 and mas[i + 1] % 10 != 9) and (mas[i] % 10 != 9 and mas[i + 1] % 10 == 9):
# 		if (mas[i] ** 2 + mas[i + 1] ** 2) < max(kol) ** 2:
# 			res.append(mas[i] ** 2 + mas[i + 1] ** 2)
# print(len(res), min(res))



# f = open(r'C:\Users\spiri\Desktop\егэ материалы\17 задание\17 задание класс\9.txt')
# mas = []
# for s in f:
# 	mas.append(int(s))
# okan = []
# for s in mas:
# 	if s % 100 == 12:
# 		okan.append(s)


# res = []
# for i in range(len(mas) - 1):
# 	if (mas[i] % 100 == 12 and mas[i + 1] % 100 != 12) or (mas[i] % 100 != 12 and mas[i + 1] % 100 == 12):
# 		if (mas[i] + mas[i + 1]) ** 2 < max(okan) ** 2:
# 			res.append(mas[i] + mas[i + 1])
# print(len(res), max(res))

# f = open(r'C:\Users\spiri\Desktop\егэ материалы\17 задание\17 задание класс\10.txt')
# mas = []
# for s in f:
# 	mas.append(int(s))
# res = []
# for i in range(len(mas) - 1):
# 	if mas[i] % 3 == 0 or mas[i + 1] % 3 == 0:
# 		res.append(mas[i] + mas[i + 1])
# print(len(res), max(res))


