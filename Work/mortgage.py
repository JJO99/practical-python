principal = 500000.0
rate = 0.05
payment = 2684.11
total_paid = 0.0
month = 0

for x in range(12):
    principal = principal * (1 + rate / 12) - (payment + 1000)
    total_paid = total_paid + (payment + 1000)
    month += 1

while principal > 0:
    principal = principal * (1 + rate / 12) - payment
    total_paid = total_paid + payment
    month += 1

print('Total paid', round(total_paid, 2))
print('소요 월 수', month)
