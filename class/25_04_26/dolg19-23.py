def g(s, p, end):
    if s<=27 and p in end:
        return True
    if s<=27 and p not in end:
        return False
    if p>max(end):
        return False
    if s>27 and ((p+1)%2) == (end[0]%2):
        return g(s-3, p+1, end) or g(s-6, p+1, end) or g(int(s/3), p+1, end)
    if s>27 and ((p+1)%2) != (end[0]%2):
        return g(s-3, p+1, end) or g(s-6, p+1, end) or g(int(s/3), p+1, end)

# for s in range(27,100):
#     if g(s, 0, [2]):
#         print(s,'otvet:31')

# for s in range(27,150):
#     if g(s,0,[1,3]):
#         print(s,'otvet:28 29')

# for s in range(27,100):
#     if g(s, 0, [2,4]) and not g(s, 0, [2]):
#         print(s,'otvet: 93')
