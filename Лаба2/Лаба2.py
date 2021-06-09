import math

while True:
    menu = int(input(  "Ведіть номер задачі від 1 до 10 або введіть: 999 для заверщення роботи "))
    if menu == 1:
        x = input(  "x =  ")
        y = input(  "y =  ")

        s = float(x) + float(y)
        r = float(x) - float(y)
        d = float(x) * float(y)

        prfloat ("Сума " + str(s) + "\n")
        prfloat ("Рiзниця " + str(r) + "\n")
        prfloat ("Добуток " + str(d) + "\n")

    if menu == 2:
        x = input(  "x =  ")
        y = input(  "y =  ")
        s = (math.fabs(float(x)) - math.fabs(float(y))) / (1 + math.fabs(float(x) * float(y)))
        prfloat ("Результат "  + str(s) + "\n")

    if menu == 3:
        x = input(  "Довжина ребра куба =  ")
        o = float(x) * float(x) * float(x) 
        s = float(x) * float(x)
        print ("Обєм куба " + str(o) + "\n")
        print ("Площа бокової поверхностi " + str(s) + "\n")

    if menu == 4:
        x = input(  "x =  ")
        y = input(  "y =  ")
        s = (float(x) + float(y)) / 2
        p = math.sqrt(float(x) * float(y) )
        print ("Сер. ариф. " + str(s) + "\n")
        print ("Сер. геом. "  + str(p) + "\n")

    if menu == 5:
        x = input(  "x =  ")
        y = input(  "y =  ")
        s = (float(x) + float(y)) / 2
        p = math.sqrt(math.fabs(float(x)) * math.fabs(float(y)) )
        print ("Сер. ариф. " + str(s) + "\n")
        print ("Сер. геом. "  + str(p) + "\n")

    if menu == 6:
        x = input(  "Катет а = ")
        y = input(  "Катет б = ")
        s = math.sqrt((float(x) * float(x)) + (float(y) * float(y)))
        p = float(x) + float(y)
        print ("Гiпотенуза "  + str(s) + "\n")
        print ("Площа "  + str(p) + "\n")

    if menu == 7:
        o1 = input(  "Обєм 1 = ")
        o2 = input(  "Обєм 2 = ")
        t1 = input(  "Температура 1 = ")
        t2 = input(  "Температура 2 = ")
        oz = float(o1) * float(o2) 
        tz = (float(o1) * float(t1) + float(o2) * float(t2)) / oz
        print ("Загальний обєм = "  + str(oz) + "\n")
        print ("Загальна температура = "  + str(tz) + "\n")


    if menu == 8:
        r = input(  "Радiус =  ")
        n = input(  "Кiлькiсть сторiн = ")
        p = 2 * float(r) * float(n) * math.sin(math.pi / float(n))* math.cos(math.pi / float(n))
        print ("Периметр = "  + str(p) + "\n")

    if menu == 9:
        r1 = input(  "Опiр 1 =  ")
        r2 = input(  "Опiр 2 =  ")
        r3 = input(  "Опiр 3 =  ")
        t = 1/float(r1) + 1/float(r2) + 1/float(r3)
        print ("Заг. опiр = "  + str(t) + "\n")

    if menu == 10:
        h = input(  "Висота = ")
        t = math.sqrt((2 * float(h)) / 9.81)
        print ("Час = "   + str(t) + "\n")
    if menu == 999:
        break
