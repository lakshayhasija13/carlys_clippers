hairstyles = ["bouffant", "pixie", "dreadlocks", "crew", "bowl", "bob", "mohawk", "flattop"]

prices = [30, 25, 40, 20, 20, 35, 50, 35]

last_week = [2, 3, 5, 8, 4, 4, 6, 2]

# Total Haircut Price
total_price = 0
for price in prices :
  total_price += price
print("Total Haircut Price:", total_price)

# Average Prices
average_price = total_price / len(prices)
print("Average Haircut Price:", average_price)

# New Haircut Prices
new_prices = [price - 5 for price in prices]
print("New Prices:", new_prices)

# Total Revenue
total_revenue = 0
for i in range(0, len(hairstyles)):
  total_revenue += prices[i] * last_week[i]
print("Total Revenue:", total_revenue)

# Average Daily Revenue
average_daily_revenue = total_revenue / 7
print("Average Daily Revenue:", average_daily_revenue)

# Cuts under 30
cuts_under_30 = [hairstyles[i] for i in range(0, len(new_prices) - 1) if new_prices[i] < 30]
print("Cuts under 30:", cuts_under_30)
