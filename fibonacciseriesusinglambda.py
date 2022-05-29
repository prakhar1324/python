n = int(input("Enter number of terms you want to be printed: "))
if n == 0:
    print()
elif n==1:
    print(0)
elif n==2:
    print(0,1,end = " ")
else:
    ls = [0,1]
    list(filter(lambda i : (ls.append(ls[-1] + ls[-2]),print(ls[i],end = "\n")),range(n)))
    
