stock_prices = [10, 7, 5, 8, 11, 9]

def get_max_profit(stock_prices):
	if len(stock_prices) <= 1:
		return 0
	max_profit = 0
	min_price = stock_prices[0]

	for price in stock_prices[1:]:
		max_profit = max(max_profit, price-min_price)
		min_price = min(min_price, price)
	return max_profit

print(get_max_profit(stock_prices))