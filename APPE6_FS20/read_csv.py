import pandas as pd

with open('csv.dat') as file:
    for line in file:
        line = line.strip()
        parts = line.split(',')
        print(parts)