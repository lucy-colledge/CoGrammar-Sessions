menu = ["coffee", "tea", "brownie", "scone"]
stock = {'coffee':10,
         'tea':25,
         'brownie': 5,
         'scone':15
         }
price = {'coffee':1.5,
         'tea':1,
         'brownie': 2.25,
         'scone':1.75
         }
total_value = 0
x= "0"
for x in range (len(menu)):
    y = (menu)[x]
    item_value = (stock[y])*(price[y])
    print(f"{y} value = {item_value}" )
    x+1
    total_value += item_value
print (f"Total Stock Value:  {total_value}")