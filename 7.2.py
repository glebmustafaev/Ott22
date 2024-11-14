info = [
    'Text for tell.',
    'Используйте кодировку utf-8.',
    'Because there are 2 languages!',
    'Спасибо!'
    ]
def custom_write(file_name,strings):
    n = 0
    elems = {}
    for i in info:
        file = open(file_name, 'a', encoding='utf-8')
        tell = file.tell()
        n += 1
        file.write(f'{i}\n')
        file.close()
        elems.update({(n, tell):i})
        return elems
result = custom_write('test.txt', info)
for elems in result.items():
  print(elems)
