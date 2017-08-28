x1 = int(input("Enter number 1: "))
x2 = int(input("Enter number 2: "))
x3 = int(input("Enter number 3: "))

if x1 == x2 and x1 == x3:
    print(3)
elif x1 == x2 or x1 == x3 or x2 == x3:
    print(2)
else:
    print(0)
