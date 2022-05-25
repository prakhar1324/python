n = int(input("Enter number of students: "))
d = {}
for i in range(1,n+1):
    name = input(f"Enter name of student with roll no. {i}: ")
    marks = int(input(f"Enter marks of student with roll no. {i}: "))
    d.update({i:{'Name':name,'Marks':marks}})
sum = 0
for i in range(1,n+1):
    sum = sum + d[i]['Marks']
print(sum)