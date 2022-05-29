from asyncore import read
g= open("abc.txt","r")
s = g.read()
k = 0
lines = s.count('\n')
words = s.count(' ')
for i in s: 
    k = k+1
print('sentences in file are',lines+1)
print('words in file are',lines + words + 1)
print('words in file are',k - lines)
g.close()

