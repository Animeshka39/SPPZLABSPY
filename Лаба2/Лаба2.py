import math

while True:
    menu = int(input(  "Ведіть номер задачі 2 Параграфу (33,38,39,43,53). 3 Параграфу (64,65,66,68,74) або введіть: 999 для заверщення роботи "))
    if menu == 33:
     x = float(input("Введіть x:= "))
    y = float(input("Введіть y:= "))
    print("A)")
    if x>y : print ("max:=x")
    else : print ("max=y")
    print("B)")
    if x<y : print ("min:=x")
    else : print ("min=y")
    print("C)")
    if x>y : print ("max:=x")
    else : print ("max=y")
    if x<y : print ("min:=x")
    else : print ("min=y") 

    if menu == 38:
     x = float(input("Введіть x число "))
    y = float(input("Введіть y число "))
    if x > y:
       print("Результат обрахунку: ", x - y)
    else:
         print("Результат обрахунку: ", y - x + 1)


    if menu == 39:
       x = float(input("Введіть x число "))
       y = float(input("Введіть y число "))
    if x > y:
     print("x > y, x = ", x)
    else:
      print("Число x = ", x)
      print("Число y = ", y)

    if menu == 43:
        a=float(input("Введіть a:="))
        b=float(input("Введіть b:="))
        c=float(input("Введіть b:="))
    if a<0 : print("Число a від'ємне")
    else : print("Квадрат числа a",a*a)
    if b<0 : print("Число b від'ємне")
    else : print("Квадрат числа a",b*b)
    if c<0 : print("Число c від'ємне")
    else : print("Квадрат числа a",c*c)


    if menu == 53:
       a = float(input("Введіть a:="))
    b = float(input("Введіть b:="))
    c = float(input("Введіть c:="))
    d = float(input("Введіть d:="))
    e = float(input("Введіть e:="))
    f = float(input("Введіть f:="))
    g = float(input("Введіть g:="))
    h = float(input("Введіть h:="))
    ab = (a-e)*(h-f)-(b-f)*(g-e)
    cd = (c-e)*(h-f)-(d-f)*(g-e)
    if (ab>0) and (cd>0) or (ab<0) and (cd<0):print("Належать одній і тієї ж півплощині")
    else: print("Не належать одній і тієї ж півплощині")


    if menu == 64:
        n = int(input("Введіть n число ( n > 99)"))
    if n < 100:
     print("Число мале")
    else:
     print("Сотень ", n / 100)


    if menu == 65:
        n = int(input("Введіть n число ( n < 100)"))
    d1 = n
    d2 = n
    if n > 10:
     d1 = n // 10
    d2 = n % 10
    if (n*n == (d1 + d2) ** 3):
     print("Квадрат числа дорівнює кубу суми");
    else:
     print("Не дорівнює")



    if menu == 66:
        k = int(input("Введіть k число "))
    m = int(input("Введіть m число "))
    z = float(input("Введіть z число "))
    x = float(input("Введіть x число "))
    y = float(input("Введіть y число "))

    if((k < m*m and k == m*m) or k > m*m):
     print("x = ", math.fabs(x))
    print("y = ", math.fabs(y))
    print("z = ", math.fabs(z))
    print("m = ", m - 0.5)
    print("k = ", k - 0.5)

    if menu == 68:
        n = int(input("Введіть n число ( n <= 9999)"))
        num = n
        rev = 0
    while (num > 0):
     d = num % 10
    rev = rev * 10 + d
    num //= 10

    if rev == n:
     print("Палиндром")
    else:
     print("Не палідром")
    num = n
    n1 = num % 10
    num //= 10
    n2 = num % 10
    num //= 10
    n3 = num % 10
    num //= 10
    n4 = num % 10
    num //= 10
    if n1 == n2 and n1 == n3 and n1 != n4:
     print("Три однакові числа")
    elif n1 == n3 and n1 == n4 and n1 != n2:
     print("Три однакові числа")
    elif n2 == n3 and n2 == n4 and n2 != n1:
     print("Три однакові числа")
    else:
     print("Не три однакові цифри")

    if n1 != n2 and n2 != n3 and n3 != n4 and n4 != n1 and n4 != n2 and n3 != n1:
     print("Всі числа різні")
    else:
     print("Є однакові числа")

    if menu == 74:
        n = int(input())
    year = ("год" if 11 <= n <= 19 or n % 10 == 1 else
          "года" if 2 <= n % 10 <= 4 else
          "лет")
    print(f"{n} {year}")
    if menu == 999:
     break
