price = 250

if price >= 300:
    price *= 0.7
    print(price)
elif 300 > price >= 200:
    price *= 0.8
    print(price)
elif 200 > price >= 100:
    price *= 0.9
    print(price)
elif 100 > price >= 0:
    price *= 0.95
    print(price)
else:
    print("Sorry, no discount.")


