from re import T


def pal(s):
    t = ""
    for i in s:
        t = i + t
    if(s == t):
        print("String is Palinndrome!")
    else:
        print("String is not Palinndrome!")

pal(input("Enter string: "))