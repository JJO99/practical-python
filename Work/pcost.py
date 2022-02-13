import csv
import sys


def portfolio_cost(filelink):
    total = 0

    f = open(filelink)
    rows = csv.reader(f)
    headers = next(rows)
    for count, line in enumerate(rows, start=1):
        record = dict(zip(headers, line))
        try:
            nshares = int(record['shares'])
            price = float(record['price'])
            total += nshares * price
        except ValueError:
            print(f'Row {count}: Error Occurred - {line}')

    return total


if len(sys.argv) == 2:
    filename = sys.argv[1]
else:
    filename = './Data/missing.csv'

cost = portfolio_cost(filename)
print('Total cost:', cost)
