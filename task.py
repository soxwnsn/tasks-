try:

    print("выберите действие:")
    print("1: поиск  по логину и паролю:")
    print("2: поиск  роли:")
    choice = int(input())

    if choice == 1:
        flag = False
        login_input = input("Введите логин:")
        password_input = input("Введите пароль:")
        with open("Пользователи.csv", "r", encoding="utf-8") as file:
            lines = file.readlines()
            for i in range(1, len(lines)):
                parts = lines[i].strip().split(",")
                fam = parts[0]
                name = parts[1]
                login = parts[2]
                password = parts[3]
                role = parts[4]

                if login == login_input and password == password_input:
                    print("Нашли Пользователя")
                    with open("output.txt", "w", encoding="utf-8") as file_out:
                        file_out.write(login)
                    flag = True
            if flag == False:
                print("Пользователь с таким логином не существует")

    if choice == 2:
        flag = False
        result=[]
        role_input = input("Введите роль")
        with open("Пользователи.csv", "r", encoding="utf-8") as file:
            lines = file.readlines()
            for i in range(1, len(lines)):
                parts = lines[i].strip().split(",") # ["Мартынов" ,"Онисим Ярославович","loginDElkc2018","BOvRGk","Менеджер по продажам"]
                role = parts[4]

                if role == role_input:
                    result.append(",".join(parts))
                    flag = True
            print(result)

        with open("output.txt", "w", encoding="utf-8") as file_out:
            for item in result:
                file_out.write(item)
        if flag == False:
            print("Пользователь с такой ролью не существует")
except ValueError as e:
    print("Введите число")
