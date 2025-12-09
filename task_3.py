def process_prices(prices, discount_percent):
    new_prices = []
    for i in prices:
        if i>0:
            new_prices.append(round(i*(1-discount_percent/100)))
    return new_prices

old_prices = [1000, -50, 300, 0, 500]
print(process_prices(old_prices, 20))