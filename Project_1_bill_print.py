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


