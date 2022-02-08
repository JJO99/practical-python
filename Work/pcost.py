total = 0

with open('./Data/portfolio.csv', 'rt') as file:
    next(file)
    for line in file:
        row = line.split(',')
        row[2] = row[2].strip('\n')
        total += int(row[1]) * float(row[2])

print('Total cost: ', total)
