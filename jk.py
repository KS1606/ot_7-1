import csv
from tabulate import tabulate
import hashlib
import uuid
import pyexcel as pe

def menu():
    """
     Данная функция позволяет пользователю выбрать действие
    1. Войти : вызов функции reg()
    2. Зарегистрироваться : вызов функции vhod()
    :return:
    """
    viborrega = int(input("""Введите действие которое хотите выполнить 
    1. Вход 
    2. Регистрация
    """))
    if viborrega == 1:
        vhod()
    if viborrega == 2:
        reg()
    else:
        print("Выбранной операции не существует")
        print("--------------------------------------")
        menu()


def reg():
    """
    Данная функция регистрирует нового пользователя и созраняет в файл его данные
    :return:
    """
    login = str(input("Введите логин: "))
    csv_path = "C:/Users/KS/PycharmProjects/pythonProject2/практическая работа №1/пользователь.csv"

    with open("пользователи.csv", 'a') as fd:
        parol = str(input("Введите пароль: "))
        provparol = str(input("Повторите пароль: "))
        if parol != provparol:
            print("Введеные пароли не совпадвют")
            print("--------------------------------------")
            reg()
        if login == "admin":
            print("Вы не можете зарегистрироваться под логином администратора")
            print("--------------------------------------")
            reg()
        else:
            salt = uuid.uuid4().hex
            print(salt)
            password = input("Введите пароль:")
            hash_password = hashlib.sha256(password.encode() + salt.encode())
            palole = hash_password.hexdigest()
        fd.write(f"\n{login},{palole},{salt},user")
        tabliza()
    fd.close()


def vhod():
    """
    Данная функция позмоляет пользователю зайти в систему для просмотра товаров
    :return:
    """
    login = str(input("Введите логин: "))
    parol = str(input("Введите пароль: "))
    if login == "admin" and parol == "admin":
        tabliza1()
    csv_path = "C:/Users/KS/PycharmProjects/pythonProject3/пользователи.csv"
    with open(csv_path) as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        next(csv_reader)
        for rok in csv_reader:
            sol = rok[2]
            hash_password = hashlib.sha256(parol.encode() + sol.encode())
            palole = hash_password.hexdigest()
            if str(rok[0]) == login and str(rok[1]) == palole:
                tabliza()
        print("Неправильно введен логин или пароль")
        print("--------------------------------------")
        menu()
        csv_file.close()


def tabliza():
    """
    Данная функция выводит сообщение!
    :return:
    """
    print("Вы вошли в личный кабинет продавца. Скоро здесь появится функционал для данной роли пользователя")
    menu()


def tabliza1():
    print("Добро пожаловать администратор.")

    csv_path = "C:/Users/KS/PycharmProjects/pythonProject3/пользователи.csv"
    with open(csv_path) as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        next(csv_reader)
        a = []
        for ro in csv_reader:
            a.append(ro)
        print(tabulate(a, headers=["Логин", "Хеш пароля", "Соль", "Роль"],
                       tablefmt="grid"))
        csv_file.close()
    izm = int(input("""Выберите действие которое хотите выполнить
        1.Вернуться к меню
        2.Изменить пароль
        """))
    if izm == 1:
        menu()
    elif izm == 2:
        dobav()
    else:
        print("Выбранной операции не существует")
        print("--------------------------------------")
        menu()




def dobav():
    """

    :return:
    """
    csv_path = "C:/Users/KS/PycharmProjects/pythonProject3/пользователи.csv"
    with open(csv_path) as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        next(csv_reader)
        login_polzov = str(input("Введите логин пользователя у которого хотите изменить пароль: "))

        for row in csv_reader:
            if str(row[0]) == login_polzov:
                b = row[2]
                stroka = str(input("Введите строку на которой находится пользователь: "))
            sheet = pe.load("пользователи.csv")
            del sheet.row[stroka]
            sheet.save_as("пользователи.csv")
            with open("пользователи.csv", 'a') as fd:
                parol = str(input("Введите пароль: "))
                provparol = str(input("Повторите пароль: "))
                if parol != provparol:
                    print("Введеные пароли не совпадвют")
                    print("--------------------------------------")
                    reg()
                else:
                    salt = b
                    print(salt)
                    hash_password = hashlib.sha256(parol.encode() + salt.encode())
                    palole = hash_password.hexdigest()
                fd.write(f"\n{login_polzov},{palole},{b},user")
            fd.close()
        else:
            print("Такого пользователя не существует!")
            tabliza1()
        csv_file.close()





menu()
