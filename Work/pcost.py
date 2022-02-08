def portfolio_cost(filelink):
    total = 0

    with open(filelink, 'rt') as file:
        next(file)
        for line in file:
            row = line.split(',')
            row[2] = row[2].strip('\n')
            total += int(row[1]) * float(row[2])

    return total


result = portfolio_cost('./Data/portfolio.csv')
print(result)