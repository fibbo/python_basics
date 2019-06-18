import random


def print_test():
    print("test")


def write_numbers():
    with open('custom_exercises/numbers.txt', 'w') as f:
        data = ['{} {}\n'.format(random.randint(1, 10000), random.randint(1, 10000)) for _ in range(1000)]
        f.writelines(data)


if __name__ == '__main__':
    write_numbers()
