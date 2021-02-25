from decimal import Decimal,ROUND_UP

rate = Decimal('1.45')
seconds = Decimal('222')    # 3*60 + 42
cost = rate*seconds / Decimal('60')
print(cost)
print(round(cost,2))

rounded = cost.quantize(Decimal('0.01'), rounding=ROUND_UP)
print(rounded)