import openpyxl

wb = openpyxl.load_workbook('.Lists_for_T.xlsx', read_only=True)

big_dict = {}


def dict_filler(sheet_name):
    sheet = wb[sheet_name]
    keys_list = []
    items_list = []
    this_dict = {}
    for i in range(2, sheet.max_row):
        temp = list(sheet[i][3].value.lower()) # оказывается, единой формы ввода данных в Переводчик нет
        for n in temp:
            if n == '\"':
                temp.remove(n)
        key = ''.join(temp)
        keys_list.append(key)
        items_list.append(sheet[i][4].value)
        this_dict[key] = items_list[keys_list.index(key)] + f', актуальность: {sheet[i][2].value}'
    big_dict.update(this_dict)
    return this_dict




