import openpyxl

wb = openpyxl.load_workbook('lists_for_translator.xlsx', read_only=True)

big_dict = {}


def get_data(sheet_name): # а какой тип данных у sheet_name? с т.з. Type Hints? + см. ниже, return
    """ Takes data from a specific sheet in a table, and
     adds it to category-specific dictionary and common dict

     """

    sheet = wb[sheet_name]
    keys_list = []
    items_list = []
    this_dict = {}
    for i in range(2, sheet.max_row):
        temp = list(sheet[i][3].value.lower())
        for n in temp:
            if n == '\"':
                temp.remove(n)
        key = ''.join(temp)
        keys_list.append(key)
        items_list.append(sheet[i][4].value)
        this_dict[key] = items_list[keys_list.index(key)] + f', актуальность: {sheet[i][2].value}'
    big_dict.update(this_dict)

    return this_dict # и снова -- какой это тип данных?
