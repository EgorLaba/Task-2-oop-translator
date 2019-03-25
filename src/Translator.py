class Translator:
    def __init__(self, dictionary):
        self.__dictionary = dictionary

    @property
    def dictionary(self):
        return self.__dictionary

    @dictionary.setter
    def dictionary(self, dictionary):
        if type(dictionary) == type(dict()):
            self.__dictionary = dictionary
        else:
            print('Словарь должен быть типа <dict>')

    def translate_word(self, word):
        if word in self.__dictionary:
            translationWord = self.__dictionary[word]
            print('{} -> {} '.format(word, translationWord))
        else:
            print('Для слова {} перевода нет d'.format(word))







