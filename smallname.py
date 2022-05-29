def name(s):
    l = s.split()
    [print(i[0].upper(), end = " ") for i in l[0:-1:1]]
    # print(l[-1][0].upper() + l[-1][1:])
    print(l[-1].capitalize())
name(input())

