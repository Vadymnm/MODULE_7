from pprint import pprint

# чтение файла 'in.txt'
file_name = 'in.txt'
file = open(file_name, mode='r+')  # mode (режим): запись в конец
file_content = file.read()
file.close()

# запись файла 'in.txt' в файл 'out2.txt'
file_name = 'out2.txt'
file = open(file_name, mode='w', encoding='utf8')
file.write(file_content)
file.close()

# чтение  и  печать  файла 'out.txt'
file_name = 'out2.txt'
with open(file_name, mode='r', encoding='utf8') as file:
    for line in file:
        print(line,end='')
print(file.closed)
print('   ---------------------------------------------------------------------------------------')
print(' Использование оператора "with" при открытии файла'
      'не требует команды  "file.close()" в конце')
print('   ----------------------------------------------------------------------------------------')