import csv


def make_report(port):
    ##########
    portfolio = []
    f = open(port)
    rows = csv.reader(f)
    next(rows)

    for row in rows:
        temp = {}

        holding = (row[0], int(row[1]), float(row[2]))
        temp['name'] = holding[0]
        temp['shares'] = holding[1]
        temp['price'] = holding[2]
        portfolio.append(temp)
    f.close()

    return portfolio


def read_price(price):
    now = {}
    f = open(price)
    rows = csv.reader(f)

    for row in rows:
        try:
            now[row[0]] = float(row[1])
        except:
            break
    f.close()

    return now


def print_report(portfolio, now):
    headers = ('Name', 'Shares', 'Price', 'Change')
    print('%10s %10s %10s %10s' % headers)
    divide = ('----------', '----------', '----------', '-----------')
    print('%10s %10s %10s %10s' % divide)

    for x in range(len(portfolio)):
        temp = [portfolio[x]['name'], portfolio[x]['shares'], "$" + str(now[portfolio[x]['name']]), round(now[portfolio[x]['name']] - portfolio[x]['price'] , 2)]
        print(f'{temp[0]:>10s} {temp[1]:>10d} {temp[2]:>10s} {temp[3]:>10.2f}')


def portfolio_report(port, price):
    p = make_report(port)
    n = read_price(price)
    print_report(p, n)


portfolio_report('./Data/portfolio.csv', './Data/prices.csv')