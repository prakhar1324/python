# s = input("Enter string: ")
# d = {}
# for i in s:
#     if i not in d:
#         d.update({i:1})
#     else:
#         d[i] += 1
# print(d)
s = input("Enter string: ")
d = dict.fromkeys(s,0)
for i in s:
    d[i] += 1
print(d)
