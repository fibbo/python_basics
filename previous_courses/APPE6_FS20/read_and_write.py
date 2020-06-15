with open('my_text_file.txt', 'w') as file:
    file.write('First line of the write operation')
    file.write('This is a line with a new-line character at the end\n')
    file.write('This is another line, on a new-line below the previous one')

with open('my_text_file.txt', 'r') as file:
    for line in file:
        line = line.strip()
        print(line)
