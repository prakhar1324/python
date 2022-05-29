a = int(input("Enter value 1: "))
b = int(input("Enter value 2: "))
print("Before swaping values are:\n"f"value 1 is = {a} value 2 is = {b}")
a = a^b
b = a^b
a = a^b
print("After swaping values are:\n"f"value 1 is = {a} value 2 is = {b}")