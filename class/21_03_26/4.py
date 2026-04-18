from operator import truediv

# x=input('введите скобки')
# def sk(x):
#     if len(x)==0:
#         return True
#     elif len(x)==1:
#         return False
#     elif x[0]=='(' and x[-1]==')':
#         return sk(x[1:-1])
#     else:
#         return False
# print(sk(x))
#
x=input('vvedite slovo')
def probel(x):
    if len(x)==0:
        return ''
    elif x[0]==' ':
        return probel(x[1:])
    else:
        return x[0]+probel(x[1:])


def sk(x):
    if len(x)==1:
        return True
    elif len(x)==0:
        return True
    elif x[0]==x[-1]:
        print(x[1:-1])
        return sk(x[1:-1])
    else:
        return False
print(sk(probel(x)))
