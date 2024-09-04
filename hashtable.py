day=("a","b","c")
price=[1,2,3]
stock_prices={}
for d,p in zip(day,price):
    stock_prices[d]=p


print(stock_prices)
