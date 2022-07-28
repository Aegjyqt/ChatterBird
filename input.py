import categories
import dictionary


class Input():
    """ Governs everything that has to do with user's input (string for translation):

    process_simplify: changes text format to lowercase, gets rid of quotation marks

    process_declension: changes category-specific identifier words to the nominative case

    process_translate: translates a string processed with the two of the above

    """

    def __init__(self, text):
        self.text = text
        self.process_simplify()
        self.process_declension()

    def process_simplify(self):
        temp = list(self.text.lower())
        for i in temp:
            if i == '\"':
                temp.remove(i)
        self.text = ''.join(temp)

    def process_declension(self):
        elements = self.text.split(' ')
        for category in categories.all_categories:
            temp_list = category.cat_ids
            for i in range(0, len(elements) - 1):
                if elements[i] in temp_list:
                    elements[i] = category.name
        self.text = ' '.join(elements)

    def process_translate(self):
        if self.text in dictionary.big_dict:
            return dictionary.big_dict[self.text]
        else:
            return 'Простите, я только учусь! Но на всякий случай, попробуем ввести в именительном падеже?'
