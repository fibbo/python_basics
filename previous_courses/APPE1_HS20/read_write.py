def print_tell(f):
    print(f.tell())

with open('new_file.data', 'r+') as f:
    print_tell(f)
    f.write('tei3343st\n')
    print_tell(f)
    f.write('test\n')
    print(f.readline())
    f.write('12345')
    print(f.tell())
    f.seek(0)
    print(f.tell())
    print(f.readline())