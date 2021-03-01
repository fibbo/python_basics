import io # input/output
import re # regex

with io.open('input.txt', 'r', encoding='utf8') as f:
    text = f.read()

lines = text.split('\n')

grab_index = r'//.*(\d+,\d+.\d+).*//<BR>'
for i in range(0, len(lines) - 1, 2):
    m = re.search(grab_index, lines[i + 1])
    corrected_index = re.sub(',', '.', m.group(1))
    lines[i] = re.sub('/<BR>', f'KP {corrected_index}.1', lines[i])
    lines[i + 1] = re.sub(grab_index, f'KP {corrected_index}.2', lines[i + 1])

with io.open('output.txt', 'w', encoding='utf8') as f:
    for line in lines:
        f.write(f'{line}\n')
