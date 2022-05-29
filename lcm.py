x = int(input())
y = int(input())
z = int(input())
n = int(input())
t = ((i,k,j) for i in range(0,x+1) for j in range(0,y+1) for k in range(0,z+1))
l = []
for a in t:
    if sum(a) != n:
        l.append(a)


# for a in l:
#     print(a,":",sum(a))
#     if n==sum(a):
#         l.remove(a)
print(l)
# for a in l:
#     if sum(a)==n:
#         l.remove(a)

# print(l)

# print(sum(l[-2]))