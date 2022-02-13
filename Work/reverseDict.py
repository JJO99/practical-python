prices = {
    'GOOG': 490.1,
    'AA': 23.45,
    'IBM': 91.1,
    'MSFT': 34.23
}
print(prices.items())

reverse = list(zip(prices.values(), prices.keys()))
print(reverse)

print(min(reverse), max(reverse), sorted(reverse))
