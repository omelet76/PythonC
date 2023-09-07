# with open('D:\Code\PythonC\9\pi_digits.txt') as file:
#     contents = file.read()
# print(contents.rstrip())

filename = 'D:\Code\PythonC\9\pi_digits.txt'
with open(filename) as file_object:
    lines = file_object.readlines()
pi = ''
for line in lines:
    pi += line.strip()
print(pi)
