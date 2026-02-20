import pyodbc
from datetime import datetime

conn = pyodbc.connect(
    "Driver={SQL Server};"
    "Server=DESKTOP-RPFEVBB\SQLEXPRESS01;"
    "Database=pythonpractice;"
    "Trusted_Connection=yes;"
)

cursor = conn.cursor()


class Account:
    def __init__(self, email):
        self.email = email

    def check_user_exists(self):
        cursor.execute("SELECT user_id FROM Users WHERE email = ?", (self.email,))
        return cursor.fetchone()

    def register_user(self, plan_name):
        try:
            cursor.execute(
                "INSERT INTO Users (email, subscription) VALUES (?, ?)",
                (self.email, plan_name)
            )
            conn.commit()
            print("User registered successfully!")
            cursor.execute("SELECT @@IDENTITY")
            return cursor.fetchone()[0]
        except:
            print("Email already registered!")
            return None

class Plans:
    def __init__(self, plan_name):
        self.plan_name = plan_name

    def get_plan_price(self):
        cursor.execute("SELECT price FROM Plans WHERE plan_name = ?", (self.plan_name,))
        result = cursor.fetchone()
        if result:
            return result[0]
        else:
            return None

class Payments:
    def __init__(self, user_id, amount):
        self.user_id = user_id
        self.amount = amount
        self.date = datetime.now()

    def make_payment(self):
        cursor.execute(
            "INSERT INTO Payments (user_id, amount, payment_date) VALUES (?, ?, ?)",
            (self.user_id, self.amount, self.date)
        )
        conn.commit()
        print("Payment Successful!")

class Movies:
    def show_movies(self):
        cursor.execute("SELECT movie_id, title FROM Movies")
        movies = cursor.fetchall()
        print("\nAvailable Movies:")
        for movie in movies:
            print(movie[0], "-", movie[1])

    def add_to_favourite(self, user_id, movie_id):
        cursor.execute("SELECT title FROM Movies WHERE movie_id = ?", (movie_id,))
        result = cursor.fetchone()

        if result:
            cursor.execute(
                "INSERT INTO Favourites (user_id, title) VALUES (?, ?)",
                (user_id, result[0])
            )
            conn.commit()
            print(result[0], "added to favourites!")
        else:
            print("invalid Movie Selection!")

print("welcome to Netflix\n")

email = input("enter your email: ")

account = Account(email)
existing_user = account.check_user_exists()

if existing_user:
    print("user already exists. logging in")
    user_id = existing_user[0]
else:
    print("\navailable Plans: Basic | Standard | Premium")
    plan_name = input("choose your plan: ")

    plan = Plans(plan_name)
    price = plan.get_plan_price()

    if price:
        print("Plan Price:", price)
        user_id = account.register_user(plan_name)

        if user_id:
            payment = Payments(user_id, price)
            payment.make_payment()
    else:
        print("Invalid Plan Selected!")
        exit()

movies = Movies()

while True:
    movies.show_movies()
    choice = int(input("Select movie ID to add favourite: "))
    movies.add_to_favourite(user_id, choice)

    more = input("Add more movies? (yes/no): ")
    if more.lower() != "yes":
        break

with open("acknowledgement.txt", "a") as file:   #ad acknowledgement for priting user details
    file.write("----- NETFLIX RECEIPT -----\n")
    file.write(f"Email: {email}\n")
    file.write(f"Login Time: {datetime.now()}\n")
    file.write("Enjoy Watching!\n")
    file.write("-----------------------------------!\n")

print("\nAcknowledgement saved successfully!")






