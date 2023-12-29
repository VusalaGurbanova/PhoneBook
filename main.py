filePath = 'PhoneBook.txt'

def show_menu():
    print( '1.Распечатать справочник\n'
          '2.nayti telefon po faylam\n'
          '3. izmenit nomer telefona\n'
          '4. udalit zapis\n'
          '5. nayti po nomeru telefona\n'
          '6. dobavit\n'
          '7. dobavit iz druqoqo spravochnika\n'
          '8. zakonchit rabotu\n', sep ='\n')
    choice = int(input('Vvedite nomer punkta menyu: '))
    return choice

def read_text(filePath):
    phone_book =[]
    fields = ['Lastname', 'Name','Phone','description']
    with open (filePath,'r', encoding = 'utf-8') as phb:
        for line in phb:
            record=dict(zip(fields, line.split(',')))
            phone_book.append(record)

    return phone_book

def write_text(filePath, phone_book):
    with open(filePath, 'w', encoding='utf-8') as pb_out:
        for index in range (0, len(phone_book)):
            string = ''
            for value in phone_book[index].values():
                string += value + ','
            pb_out.write(f'{string[:-1]}\n') 

def find_by_lastname(phone_book, lastname):
    for item in phone_book:
        if lastname == item['Lastname']:
            return item.values()
        return 'abonent ne nayden'

def add_user(phone_book, user_data):
    phone_book.append(user_data)
    write_text(filePath, phone_book)
    return 'Abonent' + user_data['Name']+ ' ' + user_data['Lastname'] + 'dobavlen'

def change_number(phone_book, lastname, new_number):
    newItem ={}
    for item in phone_book:
        if lastname == item['Lastname']:
            newItem = item
            newItem['Phone'] = new_number
            phone_book.remove(item).append(newItem)
            write_text(filePath, phone_book)
            return 'Nomer telefona abonenta' + item['Name']+ ' ' + newItem['Lastname'] + ' izmenen'
    return 'abonent ne nayden'
    
def delete_by_lastname(phone_book, lastname):
    for item in phone_book:
        if lastname == item['Lastname']:
            phone_book.remove(item)
            write_text(filePath, phone_book)   
            return 'Abonenta ' + item['Name'] + ' ' + item['Lastname'] + ' udalen'
    return 'abonent ne nayden'
    
def work_with_phonebook():
    choice = show_menu()
    phone_book = read_text(filePath)

    while(choice != 8):
        if choice ==1:
            print(phone_book)
        elif choice == 2:
            lastname = input('vvedite familiyu ')
            print(find_by_lastname(phone_book,lastname))
        elif choice == 3:
            lastname = input('vvedite familiyu: ')
            new_number = input(' vvedite nomer telefona: ')
            print(change_number(phone_book,lastname,new_number))
        elif choice == 4:
            lastname = input('vvedite nomer telefona: ')
            print(delete_by_lastname(phone_book,lastname))
        elif choice ==5:
            fields =['Lastname', 'Name','Phone','description']
            user_data ={}
            for item in fields:
                inputStr=input('Vvedite '+ item + ': ')
                if len(inputStr)== 0:
                    inputStr = input('Vvedite '+ item + ': ')
                user_data[item] = inputStr
            print(add_user(phone_book, user_data))
        elif choice ==6:
            fileName = input('Vvedite naimenovaniye fayla: ')
            if len(fileName)>0:
                phoneList = read_text(filePath)
                for index in range(0, len(phoneList)):
                    print(f'{(index+1)}.{phoneList[index]["Name"]} {phoneList[index]["Lastname"]} - {phoneList[index]["Phone"]}')
                    numberItem = (int(input('vvedite nomer stroki abonenta: ')) - 1)
                    phone_book.append(phoneList[numberItem])
                    write_text(filePath, phone_book)
        choice = show_menu()

work_with_phonebook()

            
