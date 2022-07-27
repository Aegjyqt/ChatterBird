import categories
import dictionary


class Input():
    def __init__(self, text):
        self.text = text
        self.process()
        self.process_cat()

    def process(self):
        temp = list(self.text.lower())
        for i in temp:
            if i == '\"':
                temp.remove(i)
        self.text = ''.join(temp)

    def process_cat(self):
        elements = self.text.split(' ')
        for category in categories.all_categories:
            temp_list = category.cat_ids
            for i in range(0, len(elements) - 1):
                if elements[i] in temp_list:
                    elements[i] = category.name
        self.text = ' '.join(elements)

    def translate(self):
        if self.text in dictionary.big_dict:
            return dictionary.big_dict[self.text]
        else:
            return 'Простите, я только учусь! Но на всякий случай, попробуем ввести в именительном падеже?'
