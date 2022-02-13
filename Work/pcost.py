import csv
import sys


def portfolio_cost(filelink):
    total = 0

    f = open(filelink)
    rows = csv.reader(f)
    next(rows)
    for count, line in enumerate(rows, start=1):
        try:
            total += int(line[1]) * float(line[2])
        except ValueError:
            print(f'Row {count}: Error Occurred - {line}')

    return total


if len(sys.argv) == 2:
    filename = sys.argv[1]
else:
    filename = './Data/missing.csv'

cost = portfolio_cost(filename)
print('Total cost:', cost)
