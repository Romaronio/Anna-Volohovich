# from itertools import *
# k = 0
# for w in product('кресло', repeat=4):
#     s = ''.join(w)
#     if s[0] in 'крсл' and s[-1] in 'ео':
#         k += 1
# print(k)


# from itertools import *
# k = 0
# for w in product('пуля', repeat=6):
#     s = ''.join(w)
#     if s.count('у') == 2:
#         k += 1
# print(k)


# from itertools import *
# k = 0
# for i, w in enumerate(product(sorted('мужчина'), repeat=6), start=1):
#     s = ''.join(w)
#     if s[0] != 'ж' and s.count('ч') <= 1 and i % 2 == 0:
#         k += 1
# print(k)


# from itertools import *
# k = 0
# for w in product('0123456', repeat=5):
#     s = ''.join(w)
#     for i in '0123456':
#         s = s.replace(i * 2,'*')
#     if s.count('6') == 1 and '*' not in s and s[0] != '0':
#         k += 1
# print(k)



# from itertools import *
# k = 0
# for w in permutations('0#*#*#*#*#', r=4):
#     s = ''.join(w)
#     if s[0] != '0':
#         if '**' not in s and '##' not in s and '0*' not in s and '*0' not in s:
#             k += 1
# print(k)


# from itertools import *
# k = 0
# for w in permutations('0123456789', r=4):
#     s = ''.join(w)
#     for x in '24680':
#         for y in '20468':
#             s = s.replace(x + y, '*')
#     for z in '13579':
#         for w in '13579':
#             s = s.replace(w + z, '*')
#     if '*' not in s and s[0] != '0':
#         k += 1
# print(k)



# from itertools import *
# for i, w in enumerate(product(sorted('сумка'), repeat=5)):
#     s = ''.join(w)
#     if s == 'кумас':
#         print(i, s)


#
# from itertools import *
# for i, w in enumerate(product(sorted('макс'), repeat=6), start=1):
#     s = ''.join(w)
#     if s.count('м') == 0 and s.count('с') == 0 and 'кк' not in s:
#         print(i)


#
# from itertools import *
# for i, w in enumerate(product(sorted('сентябрь'), repeat=5), start=1):
#     s = ''.join(w)
#     if s.count('ь') == 0 and s[0] == 'р' and i % 2 == 0:
#         print(i)



































