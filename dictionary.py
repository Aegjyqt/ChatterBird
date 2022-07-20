import openpyxl

wb = openpyxl.load_workbook('.Lists_for_T.xlsx', read_only=True)

big_dict = {}


def dict_filler(sheet_name):
    sheet = wb[sheet_name]
    keys_list = []
    items_list = []
    this_dict = {}
    for i in range(2, sheet.max_row):
        temp = list(sheet[i][3].value.lower())
        for i in temp:
            if i == '\"':
                temp.remove(i)
        key = ''.join(temp)
        keys_list.append(key)
    for i in range(2, sheet.max_row):
        items_list.append(sheet[i][4].value)
    for item in keys_list:
        this_dict[item] = items_list[keys_list.index(item)]
    big_dict.update(this_dict)
    return this_dict




