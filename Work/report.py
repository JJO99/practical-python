import csv


def read_portfolio(filename):
    portfolio = []

    f = open(filename)
    rows = csv.reader(f)
    next(rows)

    for row in rows:
        holding = (row[0], int(row[1]), float(row[2]))
        portfolio.append(holding)

    return portfolio

### 인터프리터에서 portfolio = read_portfolio('Data/portfolio.csv') 실행
### total = 0.0
### for name, shares, price in portfolio:
###     total += shares*price
