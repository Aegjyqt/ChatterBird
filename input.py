import dictionary, categories

class Input():
    def __init__(self, text):
        self.text = text
        self.process()
        self.process_cat()


    def process(self):
        temp = list(self.text.lower()) # приводим строку к нижнему регистру => простота поиска
        for i in temp:                 # убираем кавычки, с той же целью
            if i == '\"':
                temp.remove(i)
        self.text = ''.join(temp)      # на выходе снова строка

    def process_cat(self):             # просто заменем на тип категории, т.е. именительный падеж
        elements = self.text.split(' ')
        for category in categories.all_categories:
            temp_list = category.cat_ids
            for i in range(0, len(elements) - 1):
                if elements[i] in temp_list:
                    elements[i] = category.name
        self.text = ' '.join(elements)               # снова строка на выходе

    def translate(self):
        if self.text in dictionary.big_dict:
            return dictionary.big_dict[self.text]
        else:
            return 'Простите, я только учусь! Но на всякий случай, попробуем ввести в именительном падеже?'







