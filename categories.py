import openpyxl

import dictionary

wb = openpyxl.load_workbook('lists_for_translator.xlsx', read_only=True)
all_categories = []


class Category:
    """ Governs specific term categories

    get_ids: gets declensions of the category-specific identifier word from category-specific sheet in a table

    """

    def __init__(self, name: str):
        self.name = name
        self.cat_ids = []
        self.cat_dict = dictionary.get_data(self.name)
        self.get_ids(wb[self.name])
        all_categories.append(self)

    def get_ids(self, sheet): # а какой тип данных у sheet? с т.з. Type Hints?
        for row in range(2, 8):
            self.cat_ids.append(sheet[row][1].value)


cat_dpts = Category('управление')
cat_fclts = Category('факультет')
