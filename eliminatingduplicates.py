
# def s(l):
#     ls = []
#     for i in l:
#         if i in ls:
#             pass
#         else:
#             ls.append(i)
#     print(ls)
def s(l):
    s = set(l)
    l = list(s)
    print(l)
l = [1,2,3,4,1,2,3,4,0,5,6,4,5,7,5,8,9]
s(l)


