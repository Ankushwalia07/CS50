price = 50
inserted = 0
while inserted < price:
    print("Amount Due:", price - inserted)
    coin = int(input("Insert Coin: "))
    if coin in [5, 10, 25]:
        inserted += coin
print("Change Owed:", inserted - price)