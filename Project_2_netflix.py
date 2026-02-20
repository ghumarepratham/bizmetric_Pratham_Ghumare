
# class Account:
#     def __init__(self, id, sign_in, subscription):
#         self.id = id
#         self.sign_in = sign_in
#         self.subscription = subscription

#     def log_in_detail(self):
#         print("user", self.id, "logged in using", self.sign_in)

#     def verified_user(self):
#         print("user verified  ")

#     def user_details(self):
#         print("user id: ", self.id)
#         print("subscription: ", self.subscription)


# class Plans:
#     def __init__(self, plan_id, plan_name, price):
#         self.plan_id = plan_id
#         self.plan_name = plan_name
#         self.price = price

#     def plan_details(self):
#         print("plan: ", self.plan_name)
#         print("price: ", self.price)

#     def valid_plan(self):
#         print("plan is active")

# class Payments:
#     def __init__(self, transaction_id, trans_date, amount):
#         self.transaction_id = transaction_id
#         self.trans_date = trans_date
#         self.amount = amount

#     def payment_detail(self):
#         print(f"transaction ID:  ", self.transaction_id)
#         print(f"date: ",self.trans_date)
#         print(f"amount Paid: ", self.amount)

#     def pymt_validation(self):
#         print("Payment successful and validated")


# class FilmsSeries:
#     def __init__(self, series_id, release_date, title):
#         self.series_id = series_id
#         self.release_date = release_date
#         self.title = title
#         self.favourites = []

#     def add_to_fav(self):
#         self.favourites.append(self.title)
#         print(self.title," added to favourites",)

#     def watched_fav(self):
#         print("Watching: ",self.title)




# acc1 = Account(1, "pratham@gmail.com", "Premium")
# plan1 = Plans(101, "Premium", 799)
# pmt1 = Payments(5001, "12-02-2026", 799)
# movie = FilmsSeries(301, "2025", "Stranger Things")




# acc1.log_in_detail()
# acc1.verified_user()
# acc1.user_details()

# plan1.plan_details()
# plan1.valid_plan()

# pmt1.payment_detail()
# pmt1.pymt_validation()

# movie.add_to_fav()
# movie.watched_fav()









##Same project doing with SQL connectity


import pyodbc
from datetime import datetime

# ---------------- DATABASE CONNECTION ----------------

conn = pyodbc.connect(
    "Driver={SQL Server};"
    "Server=DESKTOP-RPFEVBB\SQLEXPRESS01;"
    "Database=pythonpractice;"
    "Trusted_Connection=yes;"
)

cursor = conn.cursor()


# ---------------- ACCOUNT CLASS ----------------
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


# ---------------- PLAN CLASS ----------------
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


# ---------------- PAYMENT CLASS ----------------
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


# ---------------- MOVIES CLASS ----------------
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
            print("Invalid Movie Selection!")


# ---------------- MAIN NETFLIX FLOW ----------------
print("Welcome to Netflix\n")

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


# ---------------- MOVIE SECTION ----------------
movies = Movies()

while True:
    movies.show_movies()
    choice = int(input("Select movie ID to add favourite: "))
    movies.add_to_favourite(user_id, choice)

    more = input("Add more movies? (yes/no): ")
    if more.lower() != "yes":
        break


# ---------------- RECEIPT ----------------
with open("acknowledgement.txt", "a") as file:
    file.write("----- NETFLIX RECEIPT -----\n")
    file.write(f"Email: {email}\n")
    file.write(f"Login Time: {datetime.now()}\n")
    file.write("Enjoy Watching!\n")
    file.write("-----------------------------------!\n")

print("\nAcknowledgement saved successfully!")






