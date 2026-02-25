# f = open(r"1.txt")
# p = 0
# for s in f:
#     k = [int(s) for s in s.split()]
#     if k[0] == k[1] or k[1] == k[2] or k[0] == k[2]:
#         p += 1
# print(p)


# f = open(r'2.txt')
# k = 0
# for s in f:
#     l = [int(i) for i in s.split()]
#     if sum(l) / 3 < 30:
#         k += 1
# print(k)


# f = open(r'3.txt')
# k = 0
# for s in f:
#     l = [int(i) for i in s.split()]
#     if (max(l) + min(l)) % 3 == 0:
#         if abs(l[0] - l[1]) == abs(l[2] - l[3]) or abs(l[0] - l[2]) == abs(l[1] - l[3]) or abs(l[0] - l[3]) == abs(l[1] - l[2]):
#             k += 1
# print(k)


# f = open(r'4.txt')
# k = 0
# for s in f:
#     l = list(map(int, s.split()))
#     l.sort()
#     if l[4] ** 2 > l[1] * l[2] * l[3] * l[0]:
#         if l[4] * l[3] / 2 > l[1] + l[2] + l[0]:
#             k += 1
# print(k)


# f = open(r'5.txt')
# for s in f:
#     l = [int(i) for i in s.split()]
#     povt = [i for i in l if l.count(i) == 3]
#     nepovt = [i for i in l if l.count(i) == 1]
#     if len(povt) == 3 and len(nepovt) == 4:
#         if max(l) in nepovt




# f = open(r'6.txt')
# k = 0
# for s in f:
#     l = [int(i) for i in s.split()]
#     povt = [i for i in l if l.count(i) == 3]
#     nepovt = [i for i in l if l.count(i) == 1]
#     if len(povt) == 3 and len(nepovt) == 4:
#         if sum(nepovt) / 4 <= povt[0]:
#             k += 1
# print(k)


f = open(r'7.txt')
k = 0
for s in f:
    l = [int(i) for i in s.split()]
    if l[0] > l[1] > l[2] > l[3] > l[4] > l[5] > l[6]:
        if (l[0] + l[6]) / 2 > (l[1] + l[2] + l[3] + l[4] + l[5]) / 5:
            k += 1
print(k)
