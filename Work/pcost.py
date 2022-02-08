def portfolio_cost(filelink):
    total = 0
    checkLine = 0
    with open(filelink, 'rt') as file:
        next(file)
        for line in file:
            checkLine += 1
            row = line.split(',')
            row[2] = row[2].strip('\n')
            if row[0] == '' or row[1] == '' or row[2] == '':
                print(f'Line {checkLine} Pass')
                continue
            total += int(row[1]) * float(row[2])

    return total


result = portfolio_cost('./Data/portfolio.csv')
print(f'Total Cost: {result}')
result = portfolio_cost('./Data/missing.csv')
print(f'Total Cost: {result}')