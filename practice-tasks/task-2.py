def calculate_total_cost(fruit_prices, fruit_quantities):
    total_cost = 0
    for fruit, quantity in fruit_quantities.items():
        if fruit in fruit_prices and quantity>0:
            total_cost += fruit_prices[fruit] * quantity
    return total_cost
    
fruit_prices = {
    "apple": 2.5,
    "banana": 1.2,
    "orange": 3.0,
    "pear": 2.8
}

fruit_quantities = {}

while(True):
    input_string = input("Enter fruit name and quantity (space separated):")
    fruit_info = input_string.split()
    
    if fruit_info[0].lstrip('-+').isdigit():
        print("Name should not be numeric!")
        
    elif not fruit_info[1].lstrip('-+').isdigit():
        print("Please provide a valid numeric quantity!")
        
    else:
        name = fruit_info[0]
        quantity = int(fruit_info[1])
        if name not in fruit_prices:
            print("We don't have a price for this fruit!")
        if quantity <= 0:
            print("Fruits in zero or negative quantities won't contribute to the total cost!")
        fruit_quantities[name] = quantity
        
    next = input("Add another fruit? (y/n) ")
    if next == "n":
        break

print(f"Your Order Summary: {fruit_quantities}")
print(f"Total Cost: ${calculate_total_cost(fruit_prices, fruit_quantities)}")