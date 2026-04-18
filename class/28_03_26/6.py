from sys import *
setrecursionlimit(3000)
def f(n):
    if n==1:
        return 1
    if n>1:
        return n*f(n-1)
print((3*f(2025)+f(2024))/f(2023))