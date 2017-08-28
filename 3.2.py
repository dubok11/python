x1 = int(input("Введите число от 1 до 8\n"))
y1 = int(input("Введите число от 1 до 8\n"))
x2 = int(input("Введите число от 1 до 8\n"))
y2 = int(input("Введите число от 1 до 8\n"))
if x1 % 2 == 1 and y1 % 2 == 1 or x1 % 2 == 0 and y1 % 2 == 0:
    x = True
else:
    x = False
if x2 % 2 == 1 and y2 % 2 == 1 or x2 % 2 == 0 and y2 % 2 == 0:
    y = True
else:
    y = False
    
if x == True and y == True:
    print("Обе клетки закрашены")
elif x == False and y == False:
    print("Обе клетки НЕ закрашены")
else:
    print("Одна клетка закрашена, вторая нет")
