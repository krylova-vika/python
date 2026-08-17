import json
import re


#переменные
choise_action = "4" #главное меню
phone = ""
name = ""
lastname = ""
comment = ""
valid_number = False
valid_name = False
index_contact = None
category_changes = "1"
#переменные для внесения изменений
phone_change = ""
name_change = ""
lastname_change = ""
comment_change = ""
approved = False
valid_number_change = False


def check_contact(phone: str) -> bool:
    """ Checking the number vor validity"""
    if phone[0:2] == "+7" and re.fullmatch('\\d{10}',phone[2:]) != None:
        print("Номер валидный")
        return True
    elif phone[0] == "8" and re.fullmatch('\\d{10}',phone[1:]) != None:
        print("Номер валидный")
        return True
    else:
        print("Номер невалидный")
        return False

def check_name(name: str) -> bool:
    """ Checking the name vor validity"""
    if name != "":
        return True
    elif name == "":
        print("Имя не должно быть пустым")
        return False

def get_data_from_file() -> dict:
    """Get data from contact file"""
    # открываем файл
    contact_file = open("../different_files/contacts.json", mode="r", encoding="utf-8")
    # записываем сведения из файла
    json_data = json.load(contact_file)
    # закрываем файл
    contact_file.close()
    return json_data

def contact_search(phone: str, json_data: dict) -> int:
    """Contact search in file"""
    index_contact = None
    for i in range(len(json_data["contacts"])):
        if json_data["contacts"][i]["phone"] == phone:
            index_contact = i
            break
    return index_contact

def save_data_to_file(json_data: dict) -> None:
    contact_file = open("../different_files/contacts.json", mode="w", encoding="utf-8")
    json.dump(json_data, contact_file, indent=4, ensure_ascii=False)
    contact_file.close()


while choise_action in ["1", "2", "3", "4"]:
    # для выбора действия
    choise_action = input("Главное меню:\n"
                          "Для создания контакта наберите - 1\n"
                          "Для изменения контакта наберите - 2\n"
                          "Для удаления контакта наберите -3\n"
                          "Выйти - 0\n")
    if choise_action in ["1", "2", "3"]:
        phone = input("Введите номер телефона: ").replace(" ", "")
        valid_number = check_contact(phone)
        if valid_number:
            if choise_action == "1":
                json_data = get_data_from_file()
                index_contact = contact_search(phone,json_data)

                # условие на наличие номера в списке
                if index_contact != None:
                    print(
                        "Такой контакт уже существует\n"
                        f"Телефон: {json_data["contacts"][index_contact]["phone"]}\n"
                        f"Имя: {json_data["contacts"][index_contact]["name"]}\n"
                        f"Фамилия: {json_data["contacts"][index_contact]["lastname"]}\n"
                        f"Комментарий: {json_data["contacts"][index_contact]["comment"]}\n")
                else:
                    # создание контакта
                    if  choise_action == "1":
                        name = input("Введите имя контакта: ")
                        valid_name = check_name(name)
                        if valid_name == True:
                            #записываем остальные сведения: фамилию и комментарий
                            lastname = input("Введите фамилию контакта (поле необязательно): ")
                            comment = input("Введите комментарий (поле необязательно): ")

                            #сохраняем это все в словарь - новый контакт
                            #new_contact = {"phone":phone, "name":name, "lastname":lastname, "comment":comment}

                            # Добавляем в наш словарь
                            json_data["contacts"].append({"phone":phone, "name":name, "lastname":lastname, "comment":comment})

                            #сохраняем контакт в файл
                            save_data_to_file(json_data)

                            print("Контакт создан")
                        valid_name = False #для повторного использования для изменений

            #изменение контакта
            elif choise_action == "2":
                json_data = get_data_from_file()
                index_contact = contact_search(phone,json_data)

                #условие на наличие номера в списке
                if index_contact == None:
                    print("Номер не существует")
                else:
                    print(
                    "Контакт найден\n"
                    f"Телефон: {json_data["contacts"][index_contact]["phone"]}\n"
                    f"Имя: {json_data["contacts"][index_contact]["name"]}\n"
                    f"Фамилия: {json_data["contacts"][index_contact]["lastname"]}\n"
                    f"Комментарий: {json_data["contacts"][index_contact]["comment"]}\n")
                    #выбор для изменения атрибутов в контакте
                    while category_changes not in ["0", "5"]:
                        category_changes = input(
                        "Для внесения изменений, выберите следующую опцию:\n"
                        "Изменить номер - 1\n"
                        "Изменить имя - 2\n"
                        "Изменить фамилию - 3\n"
                        "Изменить комментарий - 4\n"
                        "Применить изменения - 5\n"
                        "Выйти - 0\n")

                        if category_changes == "1":
                            while valid_number_change == False:
                                phone_change = input(f"Введите новый номер телефона: ").replace(" ", "")
                                valid_number_change = check_contact(phone_change)
                        elif category_changes == "2":
                            while valid_name == False:
                                name_change = input(f"Введите новое имя: ")
                                valid_name = check_name(name_change)
                        elif category_changes == "3":
                            lastname_change = input(f"Введите новую фамилию: ")
                        elif category_changes == "4":
                            comment_change = input("Введите новый комменарий: ")

                if category_changes == "5":
                    print("Проверьте сведения о контакте:\n"
                        f"Телефон: {phone_change if phone_change != "" else json_data["contacts"][index_contact]["phone"]}\n"
                        f"Имя: {name_change if name_change != "" else json_data["contacts"][index_contact]["name"]}\n"
                        f"Фамилия: {lastname_change if lastname_change != "" else json_data["contacts"][index_contact]["lastname"]}\n"
                        f"Комментарий: {comment_change if comment_change != "" else json_data["contacts"][index_contact]["comment"]}\n")

                    approved = input("Подтверждаю изменения - 1\n"
                        "Отменить изменения - 0\n")

                    if approved:
                        if phone_change != "":
                            json_data["contacts"][index_contact]["phone"] = phone_change
                        if name_change != "":
                            json_data["contacts"][index_contact]["name"] = name_change
                        if lastname_change != "":
                            json_data["contacts"][index_contact]["lastname"] = lastname_change
                        if comment_change != "":
                            json_data["contacts"][index_contact]["comment"] = comment_change

                        #записываем в сам файл
                        save_data_to_file(json_data)
                        print("Контакт изменен")
                elif category_changes == "0":
                    category_changes = "1"
                valid_number_change = False
                valid_name = False

            #удаление контакта
            elif choise_action == "3":
                #поиск контакта
                json_data = get_data_from_file()
                index_contact = contact_search(phone,json_data)

                #условие на наличие номера в списке
                if index_contact == None:
                    print("Номер не существует")
                else:
                    print(
                        "Контакт найден\n"
                        f"Телефон: {json_data["contacts"][index_contact]["phone"]}\n"
                        f"Имя: {json_data["contacts"][index_contact]["name"]}\n"
                        f"Фамилия: {json_data["contacts"][index_contact]["lastname"]}\n"
                        f"Комментарий: {json_data["contacts"][index_contact]["comment"]}\n")

                    category_changes = input(
                        "Выберите следующую опцию:\n"
                        "Удалить номер - 1\n"
                        "Выйти - 0\n")
                    #удаление номера
                    if category_changes == "1":
                        del json_data["contacts"][index_contact]
                        #применяем изменения в самом файле
                        save_data_to_file(json_data)

                        print("Контакт удален")
    elif choise_action == "0":
        pass
    else:
        print("Некорректно выбрано действие")













