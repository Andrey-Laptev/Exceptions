documents = [
{"type": "passport", "number": "2207 876234", "name": "Василий Гупкин"},
{"type": "invoice", "number": "11-2", "name": "Геннадий Покемонов"},
{"type": "insurance", "number": "10006", "name": "Аристарх Павлов"},
]

directories = {
'1': ['2207 876234', '11-2', '5455 028765'],
'2': ['10006', '5400 028765', '5455 002299'],
'3': [],
}


def people(documents):
    nmb = input('Введите номер документа: ')
    for item in documents:
        if item['number'] == nmb:
            print(item['name'])
            return
    print('Такого документа не существует.')


def list_names(documents):
    for el in documents:
        try:
            print(el['name'])
        except KeyError:
            print('! В базе есть документ(ы) без имени владельца !')


def list_doc(documents):
    for el in documents:
        print(el['type'], el['number'], el['name'])


def shelf(directories):
    nmb = input('Введите номер документа: ')
    for k, v in directories.items():
        if nmb in v:
            print('Документ находится на полке: ', k)
            return None
    print('Такого документа не существует.')


def add(documents, directories):
    nmb = input('Введите номер документа: ')
    tp = input('Введите тип документа: ')
    nm = input('Введите фамилию и имя владельца: ')
    nmb_shelf = input('Введите номер полки: ')
    doc_add = {"type":tp, "number":nmb, "name":nm}
    documents.append(doc_add)
    if nmb_shelf in directories.keys():
        directories[nmb_shelf].append(nmb)
    else:
        directories[nmb_shelf] = [nmb]

    print(documents)
    print(directories)


def main():
    command = input('Введите команду: ')

    functions = {
        'p': [people, documents],
        'l': [list_doc, documents],
        's': [shelf, directories],
        'a': [add, documents, directories],
        'n': [list_names, documents],
    }

    if command in functions.keys():
        functions[command][0](*functions[command][1:])
    else:
        print('Неизвестная команда')


if __name__ == '__main__':
    main()
