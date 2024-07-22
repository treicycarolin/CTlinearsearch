def find_lowest_stock_price(stock_prices):
  
  if not stock_prices:
      return None, None

  lowest_price = stock_prices[0][1]
  lowest_stock = stock_prices[0][0]

  for symbol, price in stock_prices:
      if price < lowest_price:
          lowest_price = price
          lowest_stock = symbol

  return lowest_stock, lowest_price

# Example stock prices list
stock_prices = [
  ("AAPL", 150),
  ("GOOGL", 2750),
  ("AMZN", 3400),
  ("MSFT", 290),
  ("TSLA", 650)
]

# Find the lowest stock price
lowest_stock, lowest_price = find_lowest_stock_price(stock_prices)

# Print the result
print(f"The stock with the lowest price is '{lowest_stock}' with a price of ${lowest_price}.")