def rev(s):
    t = ""
    for i in s:
        t = i + t
    return(t)
s = input("Enter string: ")
print(rev(s))