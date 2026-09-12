# Task Sheet No. 9.5: Apply Dictionary Methods and Keywords
# Description: Apply dictionary methods get, keys, values, items, setdefault, in, and not in.

product = {
    "id": "P001",
    "name": "Mouse",
    "price": 15.00,
    "quantity": 20
}

print("Product Name :", product.get("name"))
print("Brand        :", product.get("brand", "Not Available"))
print("Keys         :", list(product.keys()))
print("Values       :", list(product.values()))

# Membership checks
print()
print("'price' in product   :", "price" in product)
print("'brand' not in prod  :", "brand" not in product)

# setdefault
category = product.setdefault("category", "Electronics")
print("Setdefault category  :", category)
print("Updated product dict :", product)

'''
Sample Output:
Product Name : Mouse
Brand        : Not Available
Keys         : ['id', 'name', 'price', 'quantity']
Values       : ['P001', 'Mouse', 15.0, 20]

'price' in product   : True
'brand' not in prod  : True
Setdefault category  : Electronics
Updated product dict : {'id': 'P001', 'name': 'Mouse', 'price': 15.0, 'quantity': 20, 'category': 'Electronics'}
'''
