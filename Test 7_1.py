from pprint import pprint

# чтение файла 'in.txt'
file_name = 'in.txt'
file = open(file_name, mode='r+')  # mode (режим): запись в конец
file_content = file.read()
file.close()
#pprint(file_content)

# запись файла 'in.txt' в файл 'out.txt'
file_name = 'out.txt'
file = open(file_name, mode='a')
file.write(file_content)
file.close()

# чтение файла 'Pushkin.txt'
file_name = 'Pushkin.txt'
file = open(file_name, mode='r', encoding='utf8')
file_content = file.read()
file.close()
pprint(file_content)

# запись файла 'Pushkin.txt' в конец файла 'out.txt'
file_name = 'out.txt'
file = open(file_name, mode='a')
file.write(file_content)
file.close()

# чтение  и  печать  файла 'out.txt'
file_name = 'out.txt'
file = open(file_name, mode='r+')
file_content = file.read()
file.close()
pprint(file_content)
