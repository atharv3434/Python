"""
Assignment 5: Transactional Banking Ledger with SQLite & ACID Rollback Management
Scenario
A financial transaction engine executes fund transfers between accounts in a SQLite database. The engine must support ACID guarantees: if any part of a transfer fails (e.g. insufficient funds, invalid account), the entire transaction must roll back cleanly.

Problem Description
Create a custom exception TransactionError(Exception). Create a class BankingLedger that manages an accounts table (account_id TEXT PRIMARY KEY, holder_name TEXT, balance REAL) and an audit_log table (tx_id INTEGER PRIMARY KEY AUTOINCREMENT, from_acc TEXT, to_acc TEXT, amount REAL, timestamp TEXT):

create_account(account_id, holder_name, initial_deposit): Adds a new account. Raises ValueError if initial_deposit < 0.
transfer_funds(from_acc, to_acc, amount):
Executes an atomic transfer of amount from from_acc to to_acc.
Deducts amount from from_acc and adds amount to to_acc.
Records an entry in the audit_log table.
Validation & Rollback Rules:
amount must be strictly positive (> 0).
Both accounts must exist in the database.
from_acc must have a sufficient balance (>= amount).
If any condition fails, raise TransactionError and execute conn.rollback().
If all checks pass, execute conn.commit().
get_balance(account_id): Returns the current balance for the given account.
Example Walkthrough
bank = BankingLedger("bank.db")
bank.create_account("ACC101", "Arham", 5000.0)
bank.create_account("ACC102", "Lisa", 2000.0)

# Valid transfer
bank.transfer_funds("ACC101", "ACC102", 1500.0)
print(bank.get_balance("ACC101"))  # Output: 3500.0
print(bank.get_balance("ACC102"))  # Output: 3500.0

# Invalid transfer (insufficient funds) -> rolled back
try:
    bank.transfer_funds("ACC101", "ACC102", 10000.0)
except TransactionError as e:
    print(e)  # Output: Insufficient funds in account ACC101

# Balances remain untouched
print(bank.get_balance("ACC101"))  # Output: 3500.0
print(bank.get_balance("ACC102"))  # Output: 3500.0

"""


import sqlite3
from datetime import datetime

class TransactionError(Exception):
    pass


class BankingLedger:

    def __init__(self, db_path):

        self.conn = sqlite3.connect(db_path)
        self.cursor = self.conn.cursor()

        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS accounts (
                account_id TEXT PRIMARY KEY,
                holder_name TEXT,
                balance REAL
            )
        """)

        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS audit_log (
                tx_id INTEGER PRIMARY KEY AUTOINCREMENT,
                from_acc TEXT,
                to_acc TEXT,
                amount REAL,
                timestamp TEXT
            )
        """)

        self.conn.commit()

    def create_account(self, account_id, holder_name, initial_deposit):

        if initial_deposit < 0:
            raise ValueError(
                "Initial deposit cannot be negative."
            )

        self.cursor.execute("""
            INSERT INTO accounts
            (account_id, holder_name, balance)
            VALUES (?, ?, ?)
        """, (account_id, holder_name, initial_deposit))

        self.conn.commit()

    def transfer_funds(self, from_acc, to_acc, amount):

        try:

            if amount <= 0:
                raise TransactionError("Transfer amount must be greater than zero.")

            self.cursor.execute("SELECT balance FROM accounts WHERE account_id = ?",(from_acc,))

            sender = self.cursor.fetchone()

            if sender is None:
                raise TransactionError(f"Account {from_acc} does not exist.")

            self.cursor.execute("SELECT balance FROM accounts WHERE account_id = ?",(to_acc,))

            receiver = self.cursor.fetchone()

            if receiver is None:
                raise TransactionError(
                    f"Account {to_acc} does not exist."
                )

            sender_balance = sender[0]

            if sender_balance < amount:
                raise TransactionError(f"Insufficient funds in account {from_acc}")

            self.cursor.execute("""
                UPDATE accounts
                SET balance = balance - ?
                WHERE account_id = ?
            """, (amount, from_acc))

            self.cursor.execute("""
                UPDATE accounts
                SET balance = balance + ?
                WHERE account_id = ?
            """, (amount, to_acc))

            timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

            self.cursor.execute("""
                INSERT INTO audit_log
                (from_acc, to_acc, amount, timestamp)
                VALUES (?, ?, ?, ?)
            """, (from_acc, to_acc, amount, timestamp))

            self.conn.commit()

        except TransactionError:
            self.conn.rollback()
            raise

    def get_balance(self, account_id):

        self.cursor.execute("SELECT balance FROM accounts WHERE account_id = ?",(account_id,))
        row = self.cursor.fetchone()

        if row is None:
            raise TransactionError(f"Account {account_id} does not exist.")
        return row[0]


def main():

    bank = BankingLedger("bank.db")

    try:
        bank.create_account("ACC101","Arham",5000.0)
        bank.create_account("ACC102","Lisa",2000.0)

    except sqlite3.IntegrityError:
        print("Accounts already exist.")

    try:
        bank.transfer_funds("ACC101","ACC102",1500.0)

        print(bank.get_balance("ACC101"))
        print(bank.get_balance("ACC102"))

    except TransactionError as e:
        print(e)

    try:
        bank.transfer_funds("ACC101","ACC102",10000.0)

    except TransactionError as e:
        print(e)

    print(bank.get_balance("ACC101"))
    print(bank.get_balance("ACC102"))


main()