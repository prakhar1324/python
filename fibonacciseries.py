def fib(n):
    a = 0
    b = 1
    if n < 1:
        return
    print(a , end = " ")
    for i in range(1,n):
        c = a + b
        print(b , end=" ")
        a = b
        b = c
n = int(input("Enter number of terms of series: "))

fib(n)