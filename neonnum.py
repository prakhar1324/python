def neon(n):
    t = n**2
    sum = 0
    while(t>=1):
        temp = t%10
        sum = temp + sum
        t = t//10
    if sum == n:
        print("Numberr is neon")
    else:
        print("Number is not neon")
neon(int(input("Enter number: ")))

