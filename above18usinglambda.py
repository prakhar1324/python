l = [int(i) for i in input().split()]
nl = list(filter(lambda i: i >= 18,l))
print(nl)