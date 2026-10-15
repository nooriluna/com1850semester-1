# Week 1.3, Session 2: Sales Data Statistics

# We want to analyse a set of sales data in sales.csv

# Open the file and read the data
# find the:
#   - largest sale day (highest sale amount)
#   - average sale amount
#   - the widget which has been sold the most
# and print these out in a nice, human-readable format


# additional: you can calculate other sales statistics such as:
# - total sales for each region
# - most sold widget for each region
# - total sales for each widget


# Hints:
# - Remember to handle file errors
# - The first row contains headers: Date, Product, Sales_Amount, Units_Sold, Region
# - Sales amounts are stored as strings - you'll need to convert to int() for math
# - For finding the highest selling widget, use a dictionary to count units sold per product
# - For average, sum all sales amounts and divide by number of rows


import csv
sales =[]

with open("week1.3/session2/task2/3_sales_data/sales.csv", "r") as file:
    reader = csv.DictReader(file)
    for row in reader:
        sales.append({
            "date": row["Date"],
            "product": row["Product"],
            "amount": int(row["Sales_Amount"]),
            "units": int(row["Units_Sold"]),
            "region": row["Region"]
        })

highest = max(sales, key=lambda x: x["amount"])
print("highest sale:", highest)

average = sum(s["amount"] for s in sales) / len(sales)
print("average sale:", average)

most_units= max(sales, key=lambda x: x["units"])
print("most units sold:", most_units)

regions = {}

for sale in sales:
    region = sale["region"]
    regions[region] = regions.get(region, 0) + sale["amount"]

print("sales by region:", regions)