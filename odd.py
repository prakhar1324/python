n = int(input())
l = []
sum = 0
for i in range(n):
    l.append(int(input()))
for i in l:
    if i%2!=0:
        sum = sum + i
print(sum)
