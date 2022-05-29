f = open("cars.txt","w+")
n = int(input("How manny cars are there? "))

for i in range(n):
    f.write(input("Enter s.no,model,average: "))
    f.write("\n")
f.seek(0,0)
lines = f.readlines()
for line in lines:
    x = line.split(',')
    avg = int(x[-1])
    if avg >=15:
        print(line)

f.close()


