import os
while True:
    error = 0
    menufail = 0
    os.system('dir')
    menu = int(input("1-Назад \n2-Перейти в \n3-Змінити диск \n4-Створити папку \n5-Видалити папку \n6-Переіменувати \n7-Операції з файлами \n9-Вихід\n"))
    if menu == 7: menufail = int(input("1-Відкрити файл \n2-Створити \n3-Запис тексту в файл \n4-Перемістити \n5-Видалити \n9-Вихід\n" ))
    if menu == 1: os.chdir("..")
    if menu == 2: 
        a = str(input("Назва папки \n"))
        os.chdir(os.getcwd()  + "\\" + a)
    if menu == 3: 
        while error == 0:
            a = str(input("Вкажіть диск (для відміни введіть 9) \n"))
            try: 
                os.chdir(a + ":")
                error = 1
            except FileNotFoundError or OSError:
               print("Такого диску не існує виберіть інший \n")
               error = 0
            if a == "": 
                error = 1

    if menu == 4: 
        a = str(input("Вкажіть назву папки \n"))
        os.mkdir(a)
    if menu == 5: 
        while error == 0:
            a = str(input("Вкажіть назву папки (для відміни введіть 99exit)\n"))
            try: 
                os.rmdir(a)
                error = 1
            except FileNotFoundError:
               print("Такої папки не існує ")
               error = 0
            if a == "99exit": error = 1
    if menu == 6:
        while error == 0:
            a = str(input("Вкажіть назву файла або папки яку бажаєте переіменувати (для відміни введіть 99exit)\n"))
            try: 
                b = str(input("Вкажіть як бажаєте назвати \n"))
                os.rename(a, b)
                error = 1
            except FileNotFoundError:
                print("Такого файла не існує \n")
                error = 0
            if a == "99exit": error = 1

    if menufail == 1:
        while error == 0:
            a = str(input("Вкажіть назву файла (для відміни введіть 99exit)\n"))
            try: 
                os.startfile(a)
                error = 1
            except FileNotFoundError:
               print("Такого файла не існує \n")
               error = 0
            if a == "99exit": error = 1
    if menufail == 2:
            a = str(input("Вкажіть назву файла (для відміни введіть 99exit)\n"))
            if a == "99exit":continue
            open(a, "w")

    if menufail == 3:
        while error == 0:
            a = str(input("Вкажіть назву файла в який бажаєте ввести текст (для відміни введіть 99exit)\n"))
            b = str(input("Вкажіть як текст бажаєте записати \n"))
            try: 
                text_file = open(a, "a")
                text_file.write(b)
                text_file.close()
                error = 1
            except FileNotFoundError:
                print("Такого файла не існує ")
                error = 0
            if a == "99exit": error = 1

    if menufail == 4:
        while error == 0:
            a = str(input("Вкажіть назву файла який бажаєте перемістити (для відміни введіть 99exit)\n"))
            b = str(input("Вкажіть шлях переміщення "))
            try: 
                os.replace(a, b)
                error = 1
            except FileNotFoundError:
               print("Такого файла не існує ")
               error = 0
            if a == "99exit": error = 1
    if menufail == 5:
        while error == 0:
            a = str(input("Вкажіть назву файла який бажаєте видалити (для відміни введіть 99exit)\n"))
            try: 
                os.remove(a)
                error = 1
            except FileNotFoundError:
               print("Такого файла не існує ")
               error = 0
            if a == "99exit": error = 1

            
    os.system('cls ')    
    if menu == 9 or menufail == 9: 
        break



