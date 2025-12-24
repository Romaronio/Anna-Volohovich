# def free(n):
#     s = ''
#     while n > 0:
#         s = str(n % 3) + s
#         n = n // 3
#     return s
#
#
# mas = []
# for n in range(1, 1000):
#     s = free(n)
#     if n % 3 == 0:
#         s = s + s[-2:]
#     else:
#         s = s + free((n % 3) * 5)
#     s = int(s, 3)
#     if s > 178:
#         mas.append(s)
#
# print(min(mas))
#


# второй способ
# def free(n):
#     s = ''
#     while n > 0:
#         s = str(n % 3) + s
#         n = n // 3
#     return s
#
# k = 192
# for n in range(1, 1000):
#     s = free(n)
#     if n % 3 == 0:
#         s = s + s[-2:]
#     else:
#         s = s + free((n % 3) * 5)
#     s = int(s, 3)
#     if s > 178:
#         if s < k:
#             k = s
#
# print(k)

# k = 5
# for n in [5, 11, 100, 12, 8, 3]:
#     if n < k:
#         k = n
# print(k)













