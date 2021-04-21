import random


dna_alphabet = ['T', 'A', 'G', 'C']

def generate_random_dna_sequence(length):
    sequence = ''
    for _ in list(range(length)):
        sequence += dna_alphabet[random.randint(0,3)]
    return sequence


print(generate_random_dna_sequence(100))
