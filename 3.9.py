x1 = int(input("Введите x1 от 1 до 8\n"))
y1 = int(input("Введите y1 от 1 до 8\n"))
x2 = int(input("Введите x2 от 1 до 8\n"))
y2 = int(input("Введите y2 от 1 до 8\n"))

if x1 == x2 or y1 == y2 or abs (x1 - x2) == abs (y1 -y2):
    print("Yes")
else:
    print("NO")
