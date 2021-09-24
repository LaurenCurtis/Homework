import RetailItemClass as R
jacket = R.RetailItem("Jacket", '12', "59.95")

jeans = R.RetailItem("Designer Jeans",'40',"34.95")

shirt = R.RetailItem("Shirt",'20', "24.95")

print(jacket.get_description())
print(jacket.get_inventory())
print(jacket.get_price())

print(jeans.get_inventory())