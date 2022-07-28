# We will use the SQLite database
import sqlite3


# Initialize database connection and cursor
con = sqlite3.connect('db.sqlite')
cur = con.cursor()

# Create table "Users" with uid and balance rows
cur.execute('''CREATE TABLE IF NOT EXISTS Users (
                uid INTEGER,
                balance INTEGER
            )''')
con.commit()


def check_user(uid):
    # Function to check if user is in database or not

    cur.execute(f'SELECT * FROM Users WHERE uid = {uid}')
    user = cur.fetchone()
    if user:
        return True
    return False


def add_user(uid):
    # Function to insert new user into database

    # User starts with 0 balance
    cur.execute(f'INSERT INTO Users VALUES ({uid}, 0)')
    con.commit()


def get_balance(uid):
    # Function to get user balance
    cur.execute(f'SELECT balance FROM Users WHERE uid = {uid}')
    balance = cur.fetchone()[0]
    return balance


def add_balance(uid, amount):
    # Function to increase user balance

    cur.execute(f'UPDATE Users SET balance = balance + {amount} WHERE uid = {uid}')
    con.commit()
