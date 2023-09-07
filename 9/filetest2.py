filename = 'test.txt'
with open(filename, 'w') as file_object:
    file_object.write('i love programming')

with open(filename, 'a') as file_object:
    file_object.write('\n2')