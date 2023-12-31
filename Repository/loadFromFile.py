import Model.Note as nT


def read_file():
    # До этого пробовал парсить через библиотеки json и csv не додумался, как как нормально обрабатывать и выводить файл
    # решил остановиться на таком варианте
    try:
        array = []
        file = open("notes.csv", "r", encoding='utf-8')
        notes = file.read().strip().split("\n")
        for n in notes:
            split_n = n.split(';')
            note = nT.Note(
                id=split_n[0], title=split_n[1], body=split_n[2], date=split_n[3])
            array.append(note)
    except Exception:
        print('Журнал заметок пустой')
    finally:
        return array
