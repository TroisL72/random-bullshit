class Item():
    def __init__(self, name, quantity, price):
        self.name = name
        self.quantity = quantity
        self.price = price
        
    def display_info(self):
        print(self.name)
        print(self.quantity)
        print(self.price)
            
class Store():
    def __init__(self):
        self.item_data = []
        
    def store(self):
        num_item = int(input('Num Item? '))
        for i in range(num_item):
            name = input("Item's name: ")
            quantity = int(input("Item's quan: "))  
            price = float(input("Item's price: "))  
            item = Item(name, quantity, price)
            self.item_data.append(item)
            
    def option(self):
        while True:  
            print("1. Add item")
            print("2. Buy item")
            print("3. Exit store")
            choice = int(input("Choice ?: "))
            if choice == 1:
                add_item = input("What's item's name?: ")
                add_quan = int(input("How many would you like to add?: "))
                add_price = float(input("Item's price?: "))
                for item in self.item_data:
                    if add_item == item.name:
                        item.quantity += add_quan
                        print(f"{add_quan} {add_item}(s) added successfully!")
                        break
                else:
                    self.item_data.append(Item(add_item, add_quan, add_price))
                    print(f"{add_item} added successfully!")
            elif choice == 2:
                buy_item = input("What item do you want to buy?: ")
                for item in self.item_data:
                    if buy_item == item.name:
                        buy_quan = int(input("How many: "))
                        if buy_quan > item.quantity:
                            print("Not enough")
                        else:
                            total_price = buy_quan * item.price
                            print("Total price:", total_price)
                            item.quantity -= buy_quan
                            print(f"{buy_quan} {buy_item}(s) sold successfully!")
                            break
                else:
                    print("Item not found!")
            elif choice == 3:
                print("Exiting the store")
                break
            else:
                print("Invalid choice! Please select again.")
             
    def display_info(self):
        for item in self.item_data:
            item.display_info()
            
st = Store()
st.store()
st.display_info()
st.option()