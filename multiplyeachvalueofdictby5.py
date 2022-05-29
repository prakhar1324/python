d = {}
n = int(input())
for i in range(n):
    k = int(input())
    v = int(input())
    d.update({k:v})
for i in d.values():
    i *= 5
print(d)
