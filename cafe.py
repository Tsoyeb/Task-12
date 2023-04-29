# The below code will calculate the total Value of all the stock held in the cafe

# Then menu items are held as a list 
menu = ['Pizza', 'Pasta', 'Chicken_pie', 'Burger']

# The stock and price are stored as a dictionary 
stock = {'Pizza': 5,
         'Pasta': 6,
         'Chicken_pie': 7,
         'Burger': 3}

price = {'Pizza': 2.50,
         'Pasta': 5.99,
         'Chicken_pie': 4.99,
         'Burger': 3.99}

# This function takes in two dictionaries and multiplies the values in both dictionaries to create a new dictionary with the total value of each item on the menu 
def dict_mul(stock, price):
    total_value = dict()
    for v in stock:
        if v in price:
            total_value[v] = stock[v]*price[v]
    return total_value

# Prints new dictionary as well as the total sum of all the stock. 
total_stock_individual = (dict_mul(stock, price))
print(total_stock_individual)
total_stock = sum(total_stock_individual.values())
print(f'£ {total_stock}')
