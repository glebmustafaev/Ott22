from operator import index
from pprint import pprint


class WordsFinder:

    def __init__(self, file_names):
        self.file_names = file_names

    def get_all_words(self):
        all_words = {}
        j = ''
        with open(self.file_names, encoding='utf-8') as file:
            for line in file:
                for punctuation in [',', '.', '=', '!', '?', ';', ':', ' - ']:
                    line = line.replace(punctuation, '')
                j = j + line

        all_words.update({self.file_names: j.split()})

        return all_words

    def find(self,word):
        for word in j.split():
            i = word.lower()
            if i in j:
                x = j.index(i)
                print({self.file_names: x})

    # def count(self, word):
    #     for file_names, words in get_all_words().items():
    #         x = file_names.count(word)
    #         print({file_names: x})


finder2 = WordsFinder('test_file.txt')
print(finder2.get_all_words())  # Все слова
print(finder2.find('TEXT')) # 3 слово по счёту
# print(finder2.count('teXT')) # 4 слова teXT в тексте всего
