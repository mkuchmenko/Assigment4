
def convert_to_uah(amount, rate=41.5) :
    return(f"Result: {round(amount*rate)}UAH")

print(convert_to_uah(100))
print(convert_to_uah(100,38))
