n = int(input("ENter number of bottles"))
l = [int(x) for x in input().split() ]
m = max(l)
while(len(l)!=1 or sum(l)!=(m*len(l))):
    n = len(l)
    for i in range(n-3):
        if l[i]<l[i+1]:
            print(l[i])
            l.remove(l[i])
        elif l[i]>l[i+1]:
            print(l[i+1])
            l.remove(l[i+1])
# print(len(l))