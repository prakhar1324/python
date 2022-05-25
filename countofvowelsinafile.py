from asyncore import read


g = open("abc.txt","r")
# g.seek(0,0)
# print(g.tell())
s = g.read()
# print(s)
k = 0
for i in s: 
    if i in 'aeiou':
        k = k+1
print(k)
g.close()