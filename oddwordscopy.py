f = open("abc.txt","r")
g = open("new.txt","w+")
k = 1
for i in f.read().split():
    if k%2==1:
        g.write(i + " ")
    k +=1
g.seek(0)
print(g.read())
g.close()
f.close()