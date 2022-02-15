import csv

types = [str, int, float]
f = open('./Data/portfolio.csv')
rows = csv.reader(f)
headers = next(rows)
row = next(rows)

r = list(zip(types,row))

converted = []
for func, val in zip(types, row):
    converted.append(func(val))