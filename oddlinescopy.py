f = open("abc.txt","r")
g = open("new.txt","w+")
s = f.readlines()
k = 1
for i in s:
    if k%2==1:
        g.write(i)
    k +=1
g.seek(0)
print(g.read())
g.close()
f.close()