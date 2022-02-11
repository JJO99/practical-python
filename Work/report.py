import csv


def read_portfolio(filename):
    portfolio = []

    f = open(filename)
    rows = csv.reader(f)
    next(rows)

    for row in rows:
        temp = {}

        holding = (row[0], int(row[1]), float(row[2]))
        temp['name'] = holding[0]
        temp['shares'] = holding[1]
        temp['price'] = holding[2]
        portfolio.append(temp)

    return portfolio

### 인터프리터에서 portfolio = read_portfolio('Data/portfolio.csv') 실행