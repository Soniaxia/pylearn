prices = {
    "banana":4,
    "apple":3,
    "orange":1.5,
    "pear":3
}

stock = {
    "banana":6,
    "apple":0,
    "orange":32,
    "pear":15
}

food = {
    "banana":8,
    "apple":3,
    "orange":2
}

def list_fruit(fruit_prices,fruit_stock):
    for fruit in fruit_prices:
        print(fruit)
        print("售价",fruit_prices[fruit])
        print("库存",fruit_stock[fruit])

def total_money(fruit_prices,fruit_stock):
    money=0
    for fruit in fruit_prices:
        money=money+fruit_prices[fruit]*fruit_stock[fruit]
    return money

def compute_bill(food,prices,stock):
    money=0
    for fruit in food:
        if stock[fruit]>food[fruit]:
            money=prices[fruit]*food[fruit]+money
            stock[fruit]=stock[fruit]-food[fruit]
        else:
            money=stock[fruit]*prices[fruit]+money
            stock[fruit]=0

    return money

if __name__ == '__main__':
    # list_fruit(prices,stock)
    totalmoney=total_money(prices,stock)
    print(totalmoney)
    salemoney=compute_bill(food,prices,stock)
    print(salemoney)