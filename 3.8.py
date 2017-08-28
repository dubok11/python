x1 = int(input("Введите x1 от 1 до 8\n"))
y1 = int(input("Введите y1 от 1 до 8\n"))
x2 = int(input("Введите x2 от 1 до 8\n"))
y2 = int(input("Введите y2 от 1 до 8\n"))

if (x1  + 1 == x2 or x1 - 1 == x2) and (y1 + 1 == y2 or y1 - 1 == y2):
    print("Yes")
else:
    print("NO")
