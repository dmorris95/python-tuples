#Task 1

stock_data = [
    ("AAPL", "2021-01-01", 130.0),
    ("AAPL", "2021-01-02", 132.0),
    ("MSFT", "2021-01-01", 220.0),
    ("MSFT", "2021-01-02", 215.0),
    ("AAPL", "2021-01-03", 131.3),
    ("MSFT", "2021-01-03", 217.7)
]

def avg_stock(stock, stock_info):
    ret_info = ""
    avg_price = 0
    count = 0
    for st in stock_info:
        (name, st_date, price) = st
        if stock == name:
            avg_price += price
            count += 1
    avg_price = avg_price/count
    ret_info = (f"Average price for {stock} is {avg_price}")
    return ret_info    

print(avg_stock("AAPL", stock_data))