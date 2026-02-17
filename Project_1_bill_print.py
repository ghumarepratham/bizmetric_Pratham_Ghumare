
# from datetime import datetime

# def print_bill():
#     menu = {
#         "Dosa": 50,
#         "Idli": 30,
#         "Tea": 20
#     }

#     hotel = "Welcome to our Hotel"
#     print(("{:^50}".format(hotel)))
#     thanks = "Thanks For Visiting."
#     total = 0
#     bill_items = []

#     # take user input
#     while True:
#         item = input("Enter item name (Dosa/Idli/Tea): ").title()

#         if item not in menu:
#             print("Item not available in menu")
#             continue

#         qty = int(input("Enter quantity: "))
#         rate = menu[item]
#         amount = qty * rate

#         bill_items.append((item, qty, rate, amount))
#         total += amount

#         more = input("Do you want to add more items? (yes/no): ").lower()
#         if more != "yes":
#             break

#     # ---------- Prepare bill lines ----------
#     bill_lines = []

#     bill_lines.append("{:^50}".format(hotel))
#     bill_lines.append("")
#     bill_lines.append("{:<15} {:<10} {:<10} {:<10}".format("Item", "Qty", "Rate", "Amount"))
#     bill_lines.append("-" * 50)

#     for item, qty, rate, amount in bill_items:
#         bill_lines.append("{:<15} {:<10} {:<10} {:<10}".format(item, qty, rate, amount))

#     bill_lines.append("-" * 50)
#     bill_lines.append("{:<35} {:<10}".format("Total Amount", total))
#     bill_lines.append("")
#     bill_lines.append("{:^50}".format(thanks))

#     # ---------- Display bill on terminal ----------
#     print("\n")
#     for line in bill_lines:
#         print(line)

#     # ---------- Ask for print ----------
#     choice = input("\nDo you want to print the bill? (yes/no): ").lower()

#     if choice == "yes":
#         now = datetime.now()
#         filename = now.strftime("Hotel_bill_%Y-%m-%d_%H-%M-%S.txt")

#         # CHANGE THIS PATH AS PER YOUR SYSTEM
#         path = path = "C:/Users/Shree/Desktop/Bizmetric ILP/Python/Assignments/Bill print/"

#         full_path = path + filename

#         file = open(full_path, "w")
#         for line in bill_lines:
#             file.write(line + "\n")
#         file.close()

#         print(f"\nBill saved successfully at:\n{full_path}")
#     else:
#         print("\nBill not saved.")


# print_bill()











# from datetime import datetime

# def print_bill():
#     menu = {
#         "Dosa": 50,
#         "Idli": 30,
#         "Tea": 20
#     }

#     hotel = "Welcome to our Hotel"
#     print(("{:^50}".format(hotel)))
#     thanks = "Thanks For Visiting."
#     total = 0
#     bill_items = []


#     while True:
#         item = input("Enter item name (Dosa/Idli/Tea): ").title()

#         if item not in menu:
#             print("Item not available in menu")
#             continue

#         qty = int(input("Enter quantity: "))
#         rate = menu[item]
#         amount = qty * rate

#         bill_items.append((item, qty, rate, amount))
#         total += amount

#         more = input("Do you want to add more items? (yes/no): ").lower()
#         if more != "yes":
#             break

    
#     bill_lines = []

#     bill_lines.append("{:^50}".format(hotel))
#     bill_lines.append("")
#     bill_lines.append("{:<15} {:<10} {:<10} {:<10}".format("Item", "Qty", "Rate", "Amount"))
#     bill_lines.append("-" * 50)

#     for item, qty, rate, amount in bill_items:
#         bill_lines.append("{:<15} {:<10} {:<10} {:<10}".format(item, qty, rate, amount))

#     bill_lines.append("-" * 50)
#     bill_lines.append("{:<35} {:<10}".format("Total Amount", total))
#     bill_lines.append("")
#     bill_lines.append("{:^50}".format(thanks))


#     print("\n")
#     for line in bill_lines:
#         print(line)

    
#     choice = input("\nDo you want to print the bill? (yes/no): ").lower()

#     if choice == "yes":
#         now = datetime.now()
#         filename = now.strftime("Hotel_bill_%Y-%m-%d_%H-%M-%S.txt")

        
#         path = "C:/Users/Shree/Desktop/Bizmetric ILP/Python/Assignments/Bill print/"

#         full_path = path + filename

#         file = open(full_path, "w")
#         for line in bill_lines:
#             file.write(line + "\n")
#         file.close()

#         print(f"\nBill saved successfully at:\n{full_path}")
#     else:
#         print("\nBill not saved.")


# print_bill()


















# Generating Bill print using class - object Using Opps COncept and storing bill in local



from datetime import datetime


# -------- Menu Class --------
class Menu:
    def __init__(self):
        self.items = {
            "Dosa": 50,
            "Idli": 30,
            "Tea": 20
        }

    def get_price(self, item):
        return self.items.get(item, None)


# -------- Customer Order Class --------
class CustomerOrder:
    def __init__(self, customer_name, menu):
        self.customer_name = customer_name
        self.menu = menu
        self.bill_items = []
        self.total = 0

    def add_item(self, item, qty):
        rate = self.menu.get_price(item)
        if rate is None:
            print("Item not available.")
            return

        amount = rate * qty
        self.bill_items.append((item, qty, rate, amount))
        self.total += amount

    def generate_bill_lines(self):
        hotel = "Welcome to our Hotel"
        thanks = "Thanks For Visiting."

        lines = []
        lines.append("{:^50}".format(hotel))
        lines.append(f"Customer: {self.customer_name}")
        lines.append("")
        lines.append("{:<15} {:<10} {:<10} {:<10}".format("Item", "Qty", "Rate", "Amount"))
        lines.append("-" * 50)

        for item, qty, rate, amount in self.bill_items:
            lines.append("{:<15} {:<10} {:<10} {:<10}".format(item, qty, rate, amount))

        lines.append("-" * 50)
        lines.append("{:<35} {:<10}".format("Total Amount", self.total))
        lines.append("")
        lines.append("{:^50}".format(thanks))

        return lines

    def print_bill(self):
        lines = self.generate_bill_lines()
        for line in lines:
            print(line)

    def save_bill(self):
        now = datetime.now()
        filename = now.strftime(f"{self.customer_name}_%Y-%m-%d_%H-%M-%S.txt")

        path = "C:/Users/Shree/Desktop/Bizmetric ILP/Python/Assignments/Bill print/"
        full_path = path + filename

        lines = self.generate_bill_lines()

        with open(full_path, "w") as file:
            for line in lines:
                file.write(line + "\n")

        print(f"\nBill saved at:\n{full_path}")


# -------- Main Execution --------

menu = Menu()

while True:
    customer_name = input("\nEnter customer name: ")

    customer = CustomerOrder(customer_name, menu)

    while True:
        item = input("Enter item name (Dosa/Idli/Tea): ").title()
        qty = int(input("Enter quantity: "))

        customer.add_item(item, qty)

        more = input("Add more items? (yes/no): ").lower()
        if more != "yes":
            break

    print("\n")
    customer.print_bill()

    save = input("\nSave bill? (yes/no): ").lower()
    if save == "yes":
        customer.save_bill()

    next_customer = input("\nNext customer? (yes/no): ").lower()
    if next_customer != "yes":
        break


















##Hotel bill printing and storing data in database all included in this



from datetime import datetime
import pyodbc


class Database:
    def __init__(self):
        self.conn = pyodbc.connect(
            "Driver={SQL Server};"
            "Server=DESKTOP-RPFEVBB\SQLEXPRESS01;"  
            "Database=pythonpractice;"         
            "Trusted_Connection=yes;"
        )
        self.cursor = self.conn.cursor()

    def save_customer(self, name, total):
        now = datetime.now()

        self.cursor.execute("""
            INSERT INTO Customers (CustomerName, BillDate, TotalAmount)
            OUTPUT INSERTED.CustomerID        
            VALUES (?, ?, ?)
        """, (name, now, total)) 

        customer_id = self.cursor.fetchone()[0]
        self.conn.commit()

        return customer_id


    def save_items(self, customer_id, bill_items):
        for item, qty, rate, amount in bill_items:
            self.cursor.execute(
                "INSERT INTO BillItems (CustomerID, ItemName, Quantity, Rate, Amount) VALUES (?, ?, ?, ?, ?)",
                (customer_id, item, qty, rate, amount)
            )
        self.conn.commit()



class Menu:
    def __init__(self):
        self.items = {
            "Dosa": 50,
            "Idli": 30,
            "Tea": 20
        }

    def get_price(self, item):
        return self.items.get(item, None)


class CustomerOrder:
    def __init__(self, customer_name, menu):
        self.customer_name = customer_name
        self.menu = menu
        self.bill_items = []
        self.total = 0

    def add_item(self, item, qty):
        rate = self.menu.get_price(item)
        if rate is None:
            print("Item not available.")
            return

        amount = rate * qty
        self.bill_items.append((item, qty, rate, amount))
        self.total += amount

    def print_bill(self):
        print("\n" + "=" * 40)
        print(f"Customer: {self.customer_name}")
        print("=" * 40)
        print("{:<15} {:<10} {:<10} {:<10}".format("Item", "Qty", "Rate", "Amount"))
        print("-" * 40)

        for item, qty, rate, amount in self.bill_items:
            print("{:<15} {:<10} {:<10} {:<10}".format(item, qty, rate, amount))

        print("-" * 40)
        print("Total Amount: ",self.total)
        print("=" * 40)

    def save_to_database(self, db):
        customer_id = db.save_customer(self.customer_name, self.total)
        db.save_items(customer_id, self.bill_items)
        print("Bill saved ino database succesfully")


# -------- Main Execution --------

menu = Menu()      #objet crete
db = Database()    #same here

while True:
    customer_name = input("\nenter customer name: ")
    customer = CustomerOrder(customer_name, menu)

    while True:
        item = input("enter item name (Dosa/Idli/Tea): ").title()
        qty = int(input("enter quantity: "))
        customer.add_item(item, qty)

        more = input("add more items? (yes/no): ").lower()
        if more != "yes":
            break

    customer.print_bill()

    save = input("save bill to database.? (yes/no): ").lower()
    if save == "yes":
        customer.save_to_database(db)

    next_customer = input("next customer (yes/no): ").lower()
    if next_customer != "yes":
        break


