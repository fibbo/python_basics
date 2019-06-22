file_handle = open('text_file.txt', 'r')

for line in file_handle:
    line = line.strip()
    print(line)

file_handle.close()

print('abc')
print('123')