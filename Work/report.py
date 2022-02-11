import csv


def read_prices(filename):
    portfolio = {}

    f = open(filename)
    rows = csv.reader(f)

    for row in rows:
        try:
            portfolio[row[0]] = float(row[1])
        except:
            break

    return portfolio


a = read_prices('./Data/prices.csv')
print(a)