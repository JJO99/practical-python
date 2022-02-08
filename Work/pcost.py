import csv


def portfolio_cost(filelink):
    total = 0
    checkLine = 0

    f = open(filelink)
    rows = csv.reader(f)
    next(rows)
    for line in rows:
        checkLine += 1
        if line[0] == '' or line[1] == '' or line[2] == '':
            print(f'Line {checkLine} Pass')
            continue
        total += int(line[1]) * float(line[2])

    return total


result = portfolio_cost('./Data/portfolio.csv')
print(f'Total Cost: {result}')
result = portfolio_cost('./Data/missing.csv')
print(f'Total Cost: {result}')
