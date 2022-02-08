import csv
import sys


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


if len(sys.argv) == 2:
    filename = sys.argv[1]
else:
    filename = './Data/portfolio.csv'

cost = portfolio_cost(filename)
print('Total cost:', cost)

### 이 코드는
### python3 /Users/(계정명)/PycharmProjects/practical-python/Work/pcost.py /Users/(계정명)/PycharmProjects/practical-python/Work/Data/portfolio.csv
### 을 터미널에서 실행해야 한다.
### 파이참에서 그냥 실행하면 결과가 주르륵 나오고, 터미널에서 세번째 인자 없이 실행하면 오류 발생?