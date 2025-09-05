kiloUsed = int(input("Enter the kilowatt hours used: "))

rate1 = 7.633
rate2 = 9.259

if kiloUsed <= 1000:
    total_cents = kiloUsed * rate1
else:
    total_cents = (1000 * rate1) + ((kiloUsed - 1000) * rate2)

total_dollars = total_cents / 100

print(f"{total_dollars: .2f}")
