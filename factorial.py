n = int(input("Enter a number: "))
l = [n]
list(map(lambda i: l.append(l[-1]*i),range(n-1,1,-1)))
print(l[-1])