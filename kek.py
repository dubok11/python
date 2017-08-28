from random import *
x = randint(0, 100)
y = randint(0, 100)
print("x =",x,"\ny =",y)
if x > y:
    print(y," - наименьшее число")
elif x < y:
    print(x," - наименьшее число")
else:
    print("числа равны")
