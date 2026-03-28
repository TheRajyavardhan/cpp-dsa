
def max_profit(prices):
  min_prices = float('inf')
  max_profit = 0

  for price in prices:
    if price < min_prices:
      min_prices = price

    profit = price - min_prices

    if profit > max_profit:
      max_profit = profit

  return max_profit

prices = [7,1,5,3,6,4]
print(f"Max Profit: {max_profit(prices)}")

# time complexity = O(n)

