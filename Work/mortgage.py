principal = 500000.0
rate = 0.05
payment = 2684.11
total_paid = 0.0
month = 0

extra_payment_start_month = 61
extra_payment_end_month = 108
extra_payment = 1000

while principal > 0:
    if principal < payment:
        total_paid = total_paid + principal
        principal = 0
        month += 1

    else:
        principal = principal * (1 + rate / 12) - payment
        total_paid = total_paid + payment
        month += 1

    if extra_payment_start_month <= month <= extra_payment_end_month:
        principal -= extra_payment
        total_paid += extra_payment

    print(month, round(total_paid, 2), round(principal, 2))

print(f'Total pad: {round(total_paid, 2)}\nMonths: {month}')