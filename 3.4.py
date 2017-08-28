x1 = int(input("Enter number 1: "))
x2 = int(input("Enter number 2: "))
x3 = int(input("Enter number 3: "))

if x1 < x2 and x1 < x3:
    print(x1, "наименьшее число")
elif x2 < x1 and x2 < x3:
    print(x2, "наименьшее число")
else:
    print(x3, "наименьшее число")
