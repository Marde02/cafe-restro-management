menu = {
    "Pizza":80,
    "Coffee":50,
    "Pasta":60,
    "Salad":50
}
order_total= 0
print("Welcome to Python Restaurant")
print("Pizza: 80rs\nCoffee: 50rs\nPasta: 60rs\nSalad: 50rs")

item1=input("Select your first order= ")
if item1 in menu:
    order_total += menu[item1]
    print(f"Your order is {item1} has been added")
else:
    print(f"{item1} not present in menu!!")

another_order=input("Do you want to add another item Y/N :")
if another_order.lower() == "y":
    item2=input("select your second item= ")
    if item2 in menu:
        order_total += menu[item2]
        print(f"Item {item2} has been added to order")
    else:
        print(f"{item2} not present in menu!!")

print(f"The total amount to pay is {order_total}")



