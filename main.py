class Tokenizer:
    def __init__(self, text):
        self.text = text
        self.punctuation_list = [',', ';', ':', '.', '!', '?']
        self.punctuation_list_at_end = ['.', '!', '?']
        self.special_character_list = ['@', '#', '$', '%', '^', '&', '*', '-', '_', '+', '=']

    def __split_text(self, delimiter, strip=False, skip_delimiter=False, punctuation_as_item=False,):
        temporary_text = ''
        result = []

        if delimiter == '':
            for character in self.text:
                if strip and character == ' ':
                    continue

                result.append(character)

            return result

        def append_text(temporary_text, result, character):
            if skip_delimiter:
                temporary_text = temporary_text[:-1]

            if temporary_text:
                result.append(temporary_text.strip() if strip else temporary_text)

            if punctuation_as_item and character in self.punctuation_list:
                result.append(character)

        for character in self.text:
            temporary_text += character

            if type(delimiter) is type(list()):
                if character in delimiter:
                    append_text(temporary_text, result, character)
                    temporary_text = ''

            if character == delimiter or (punctuation_as_item and character in self.punctuation_list + self.punctuation_list_at_end):
                append_text(temporary_text, result, character)
                temporary_text = ''

        if temporary_text:
            result.append(temporary_text)

        return result

    def by_sentence(self):
        return self.__split_text(self.punctuation_list_at_end, strip=True)

    def by_word(self):
        return self.__split_text(' ', skip_delimiter=True, punctuation_as_item=True)

    def by_custom_delimiter(self, delimiter):
        return self.__split_text(delimiter, skip_delimiter=True)

    def by_character(self, strip=False):
        return self.__split_text('', strip=strip)


if __name__ == '__main__':
    dummy_text = ('Life, yellow fever, and power! The power - very strong - of the yellow fever.'
                  ' Yellow fever is a disease. Wait, is it a disease? Yes, it is a disease.')

    tokenizer = Tokenizer(dummy_text)

    print("Original text: ", dummy_text)
    print("By sentence: ", tokenizer.by_sentence())
    print("By word: ", tokenizer.by_word())
    print("By custom delimiter: ", tokenizer.by_custom_delimiter(','))
    print("By character: ", tokenizer.by_character())
    print("By character (stripped): ", tokenizer.by_character(strip=True))
