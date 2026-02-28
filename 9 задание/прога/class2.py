# 1)

# f = open(r'1.txt')
# k = 0
# for s in f:
#     m = [int(i) for i in s.split()]
#     if m[0] == m[1] or m[1] == m[2] or m[2] == m[0]:
#         k += 1
# print(k)
from itertools import permutations


# 2)
# f = open(r'2.txt')
# k = 0
# for s in f:
#     m = [int(i) for i in s.split()]
#     if sum(m) / 3 < 30:
#          k = k + 1
# print(k)


# 3)
# f = open(r'3.txt')
# k = 0
# for s in f:
#     m = [int(i) for i in s.split()]
#     if (max(m) + min(m)) % 3 == 0:
#         if abs(m[0] - m[1]) == abs(m[2] - m[3]) or abs(m[0] - m[2]) == abs(m[1] - m[3]) or abs(m[0] - m[3]) == abs(m[1] - m[2]):
#             k += 1
# print(k)


# 4)
# f = open(r'4.txt')
# k = 0
# for s in f:
#     m = [int(i) for i in s.split()]
#     m.sort()
#     # if max(m) ** 2 > (m[0] * m[1] * m[2] * m[3] * m[4]) / max(m):
#     if m[4] ** 2 > m[0] * m[1] * m[2] * m[3]:
#         if m[4] + m[3] > 2 * (m[0] + m[1] + m[2]):
#             k += 1
# print(k)


# f = open(r"5.txt")
# k = 0
# for s in f:
#     m = [int(i) for i in s.split()]
#     povt = [i for i in m if m.count(i) == 3]
#     nepovt = [i for i in m if m.count(i) == 1]
#     if len(povt) == 3 and len(nepovt) == 4:
#         if max(m) in nepovt:
#             k += 1
# print(k)














# m = [1, 1, 1, 2, 2, 2]
#
# m = [1, 2, 3, 1, 1, 1, 2, 3, 1, 2]
# n = set(m)
# print(n)

# f = open(r'6.txt')
# for s in f:
#     m = [int(i) for i in s.split()]
#     povt = [i for i in m if m.count(i) == 3]
#     nepovt = [i for i in m if m.count(i) == 1]
#     if len(set(povt)) == 1 and len(nepovt) == 4:
#         if sum(nepovt) / 4 <= povt[2]:
#             print(sum(m))


#
# f = open(r'7.txt')
# for s in f:
#     m = [int(i) for i in s.split()]
#     if m[0] > m[1] > m[2] > m[3] > m[4] > m[5] > m[6]:
#         if (m[0] + m[6]) / 2 > sum(m[1:6]) / 5:
#             print(sum(m))
#             break



# f = open(r'8.txt')
# k = 0
# for s in f:
#     m = [int(i) for i in s.split()]
#     povt = [i for i in m if m.count(i) == 3]
#     nepovt = [i for i in m if m.count(i) == 1]
#     if len(povt) == 6 and len(nepovt) == 1:
#         if max(povt) > nepovt[0]:
#             k += 1
# print(k)

