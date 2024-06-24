def work_with_phonebook():
    choice = show_menu()

    phone_book = read_txt('phon.txt')

    while (choice != 7):

        if choice == 1:
            print_result(phone_book)
        elif choice == 2:
            last_name = input('lastname ')
            print(find_by_lastname(phone_book, last_name))
        elif choice == 3:
            last_name = input('lastname ')
            new_number = input('new number ')
            print(change_number(phone_book, last_name, new_number))
        elif choice == 4:
            lastname = input('lastname ')
            print(delete_by_lastname(phone_book, lastname))
        elif choice == 5:
            number = input('number ')
            print(find_by_number(phone_book, number))
        elif choice == 6:
            user_data = input('new data ')
            add_user(phone_book, user_data)
            write_txt('phonebook.txt', phone_book)
        elif choice == 7:
            source_file = input('Enter source file name: ')
            dest_file = input('Enter destination file name: ')
            line_number = int(input('Enter line number to copy: '))
            copy_line(source_file, dest_file, line_number)

        choice = show_menu()

def show_menu():
    print("\nВыберите необходимое действие:\n"
          "1. Отобразить весь справочник\n"
          "2. Найти абонента по фамилии\n"
          "3. Найти абонента по номеру телефона\n"
          "4. Добавить абонента в справочник\n"
          "5. Удалить абонента по фамилии\n"
          "6. Изменить номер телефона абонента\n"
          "7. Скопировать данные из одного файла в другой\n"
          "8. Закончить работу")
    choice = int(input())
    return choice

def read_txt(filename):
    phone_book = []
    fields = ['Фамилия', 'Имя', 'Телефон', 'Описание']

    with open(filename, 'r', encoding='utf-8') as phb:
        for line in phb:
            record = dict(zip(fields, line.strip().split(',')))
            phone_book.append(record)

    return phone_book

def write_txt(filename, phone_book):
    with open(filename, 'w', encoding='utf-8') as phout:
        for i in range(len(phone_book)):
            s = ''
            for v in phone_book[i].values():
                s = s + v + ','
            phout.write(f'{s[:-1]}\n')

def copy_line(source_file, dest_file, line_number):
    with open(source_file, 'r', encoding='utf-8') as src, open(dest_file, 'a', encoding='utf-8') as dest:
        lines = src.readlines()
        if 0 < line_number <= len(lines):
            dest.write(lines[line_number - 1])
        else:
            print("Invalid line number")

def print_result(phone_book):
    for record in phone_book:
        print(record)

def find_by_lastname(phone_book, last_name):
    return [record for record in phone_book if record['Фамилия'].strip() == last_name]

def change_number(phone_book, last_name, new_number):
    for record in phone_book:
        if record['Фамилия'].strip() == last_name:
            record['Телефон'] = new_number
            return f"Number changed for {last_name}"
    return f"No entry found for {last_name}"

def delete_by_lastname(phone_book, last_name):
    for record in phone_book:
        if record['Фамилия'].strip() == last_name:
            phone_book.remove(record)
            return f"Deleted entry for {last_name}"
    return f"No entry found for {last_name}"

def find_by_number(phone_book, number):
    return [record for record in phone_book if record['Телефон'].strip() == number]

def add_user(phone_book, user_data):
    fields = ['Фамилия', 'Имя', 'Телефон', 'Описание']
    record = dict(zip(fields, user_data.split(',')))
    phone_book.append(record)

work_with_phonebook()
