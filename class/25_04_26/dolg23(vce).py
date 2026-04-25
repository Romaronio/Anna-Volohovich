from math import *
# 1
# def f(start, end):
#     if start<end or start==8:
#         return 0
#     if start==end:
#         return 1
#     if start>end:
#         return f(start-1, end)+f(start-4, end)+f(start//3, end)
# print(f(19,14)*f(14, 2),'otv:69')

# 2
# def f(start, end):
#     if start<end or start==7:
#         return 0
#     if start==end:
#         return 1
#     if start>end:
#         return f(start-1,end) + f(start-4,end) + f(start//3, end)
# print(f(19,13)*f(13,2), 'otv:68')

# 3
# def f(start, end):
#     if start> end or start == 56:
#         return 0
#     if start==end:
#         return 1
#     if start<end:
#         return f(start+3, end)+ f(start+7, end)+ f(start*3, end)
# print(f(12,40)*f(40,72)*f(72,89), 'otv:324')

# 4
# def f(start, end):
#     if start<end or start==26 or start==30:
#         return 0
#     if start==end:
#         return 1
#     if start>end:
#         return f(start-3, end)+f(ceil(start/2),end)
# print(f(69,14), 'otv:5')

# 5
# def f(start, end):
#     if start<end:
#         return 0
#     if start==end:
#         return 1
#     if start>end:
#         return f(start-1, end)+ f(start//2, end)
# print(f(89,30)*f(30,7), 'otv:682')

# 6
# def f(start, end):
#     if start>end:
#         return 0
#     if start==end:
#         return 1
#     if start<end:
#         return f(start+2,end)+ f(start+3, end)+f(start+4,end)
# print(f(5,11)*f(11,22)*f(22,33)*f(33,37), 'otv:4608')

# 7
# def f(start, end):
#     if start<end or start==28:
#         return 0
#     if start==end:
#         return 1
#     if start>end and start%2==0:
#         return f(start/2,end)+f(start-2,end)
#     if start>end and start%2==1:
#         return f(start-2, end)+f(start-3,end)
# print(f(98,1),'otv:12318')

# 8
# def f(start, end):
#     if start< end:
#         return 0
#     if start == end:
#         return 1
#     if start>end:
#         return f(start-1, end)+f(start//2, end)+f(start//3, end)
# print((f(106,61)*f(61,6))+(f(106,48)*f(48,6)), 'otvet: 4774')

# 9
# def f(start, end):
#     if start<end:
#         return 0
#     if start ==end:
#         return 1
#     if start> end:
#         return f(start-3, end)+f(start-4, end)+f(start//2,end)
# print((f(78,42)*f(42,2))+(f(78,30)*f(30,2))+(f(78,42)*f(42,30)*f(30,2)),'otv:4131933')

10
def f(start,end):
    if start<end:
        return 0
    if start == end:
        return 1
    if start>end:
        return f(start-3, end)+f(start-5, end)+f(start//3,end)
print((f(80,38)*f(38,3))+(f(80,18)*f(18,3))+(f(80,38)*f(38,18)), 'otv:227270')