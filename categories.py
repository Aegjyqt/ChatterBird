import dictionary
import openpyxl

wb = openpyxl.load_workbook('.Lists_for_T.xlsx', read_only=True)
all_categories = []


class Category:
    def __init__(self, name):
        self.name = name
        self.cat_ids = []
        self.cat_dict = dictionary.dict_filler(self.name)
        self.get_ids(wb[self.name])
        all_categories.append(self)

    def get_ids(self, sheet):
        for row in range(2, 8):
            self.cat_ids.append(sheet[row][1].value)

cat_dpts = Category('управление')
cat_fclts = Category('факультет')

