menu = ['toast', 'lemon', 'sandwich', 'water']

stock = {'toast': 3,
         'lemon': 6,
        'sandwich': 10,
        'water': 5}

price = {'toast': 2,
         'lemon': 1,
        'sandwich': 3,
        'water': 2}

total_stock = 0

for items in menu:
 total_stock += (stock[items] * price[items])

print(total_stock)