import io
from pprint import pprint
def custom_write(file_name, strings):
    file_name = f'Text.txt'
    number_line = 1
    strings_position = {}
    file = open(file_name, 'w', encoding='utf-8')
    for string in strings:
        byte_line = file.tell()
        file.write(f"{string}\n")
        strings_position[(number_line, byte_line)] = string
        number_line += 1
    file.close()
    return strings_position

info = [
    'Text for tell.',
    'Используйте кодировку utf-8.',
    'Because there are 2 languages!',
    'Спасибо!'
    ]

result = custom_write('test.txt', info)
for elem in result.items():
  print(elem)