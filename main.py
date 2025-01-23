# Должны сохранять/получать/изменять/удалять данные
# Данные хранятся в словаре в виде string : int
# Значения ключей и значений должны быть уникальные
from random import choice
from sys import flags
#to do
# 1) # Безопасно получить значение по ключу с использованием метода get().
# print(person_dict.get("name"))
# 2) изменить phonebook:
# keys = ["name", "phone"]
#default_value = None
#phonebook = dict.fromkeys(keys, default_value)
# 3) подумать над менюшкой - когда какие опции предлагать
phonebook = {}

def add_phone(name, phone, mydict):
    if check_key(name, mydict):
        return  print(f"Этот контакт уже записан с номером {mydict[name]}.")
    elif check_phone(phone, mydict):
        return print(f"Этот номер уже записан у контакта(тов).")
    else:
        mydict[str(name)] = str(phone)
        return print(f"Был добавлен новый контакт: {name} с номером: {phone}.")


def delete_phone_on_name(key,mydict):
    #key = input("Введите имя контакта, которого хотите удалить:")
    if check_key(key, mydict):
        del mydict[key]
        print(f"Контакт \"{key}\" был удален.")
    else:
        print(f"Контакта \"{key}\" нет в вашем телефонном справочнике.")


def get_phonebook():
    if len(phonebook):
        print("Ваш список контактов:")
        for key, value in phonebook.items():
          print(f"{key}: {value}")
    else:
        print("Телефонный справочник пуст.")


def update_phone(key, new_number, mydict):
    if check_phone(new_number, mydict):
        return print(f"Этот номер уже записан у контакта(тов).")
    elif check_key(key, mydict):
        mydict[str(key)] = str(new_number)
        return print(f"Был обновлен контакт: \"{key}\": {new_number}.")
    else:
        mydict[str(key)] = str(new_number)
        return print(f"Поскольку не был найден контакт, то был создан новый контакт: \"{key}\": {new_number}.")


# Вспомогательные функции
def check_key(key, mydict):
    if key in mydict:
        return True
    else:
        return False


def check_phone(number, mydict):
    if any(value == number for value in mydict.values()):
        return True
    else:
        return False


def app_phonebook():
    while True:
        choice = int(input("Выберете команду:\n1. Получить список контактов.\n2. Добавить контакт.\n3. Обновить контакт.\n4. Удалить контакт.\n5. Проверить есть ли контакт по имени и номеру телефона.\n6. Выйти из телефонного справочника.\n"))
        if choice == 1:
            get_phonebook()
        elif choice == 2:
            name = input("Введите имя нового контакта: ")
            phone_number = str(input("Введите номер телефона нового контакта: "))
            add_phone(name, phone_number, phonebook)
        elif choice == 3:
            name = input("Введите имя контакта:")
            phone_number = str(input("Введите номер телефона контакта: "))
            update_phone(name, phone_number, phonebook)
        elif choice == 4:
            name = input("Введите имя контакта для удаления: ")
            delete_phone_on_name(name, phonebook)
        elif choice == 5:
            data = input("Введите имя контакта, которого вы бы хотели проверить: ")
            flag_key = check_key(data, phonebook)
            flag_phone = check_phone(data, phonebook)
            if flag_key:
                print(f"Данный контакт {data} есть в справочнике с номером телефона: {phonebook[data]}.")
            elif flag_phone:
                print(f"Данный номер телефона {data} есть в справочнике.")
            else:
                print("Данного контакта или номера телефона нет в справочнике.")
        elif choice == 6:
            print("Вы вышли из справочника.")
            break
        else:
            print("Повторите команду.")


def test_cases():
  print("Начнем тестирование!")
  get_phonebook()
  add_phone("Masha", "89991221211", phonebook)
  add_phone("Masha", "89991221211", phonebook)
  add_phone("Masha1", "89991221211", phonebook)
  add_phone("Masha", "89991221222", phonebook)
  get_phonebook()
  delete_phone_on_name("Masha", phonebook)
  delete_phone_on_name("Masha", phonebook)
  get_phonebook()
  add_phone("Masha", "89991221222", phonebook)
  get_phonebook()
  update_phone("Masha1", "8888888888888", phonebook)
  get_phonebook()
  update_phone("Masha", "89991000000", phonebook)
  get_phonebook()


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    #test_cases()
    app_phonebook()