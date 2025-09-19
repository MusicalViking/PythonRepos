"""
Program Name : Assignment #8
Program description : Simulates a banking app for a checking and savings account
Author: Arthur Belanger
Date created: 4-26-25
Notes: I had a hell of a time meeting all of the guidelines for the assignment but this was similar to an
address/contact book program I made out of one of the books I had so I kind of had the foundation down
for this already.

"""
import time
divider = ("_ _ _ ")
print(divider * 3)

class BankAccount:
    def __init__(self, label):
        self.label = label
        self.balance = 0.00

    def deposit(self, amount):
        if amount < 0:
            print("Error: Deposit must be positive amount.")
        else:
            self.balance += amount
            print(f"Deposited ${amount:.2f} into {self.label}.")

    def withdraw(self, amount):
        if amount < 0:
            print("Error: Withdrawal amount can't be negative.")
        elif amount > self.balance:
            print(f"Error: Can''t withdraw ${amount:.2f} from {self.label} due to insufficient funds.")
        else:
            self.balance -= amount
            print(f"Withdrew ${amount:.2f} from {self.label}.")

    def getBalance(self):
        return self.balance

    def transfer(self, amount, other):
        if amount < 0:
            print("Error: Transfer amount must be positive amount.")
        elif amount > self.balance:
            print(f"Error: Can''t transfer ${amount:.2f} from {self.label} due to insufficient funds.")
        else:
            self.withdraw(amount)
            other.deposit(amount)
            print(f"Transferred ${amount:.2f} from {self.label} to {other.label}.")
            
    def __str__(self):
        return f"Account: {self.label}, Balance: ${self.balance:.2f}"

def main():
    Checking = BankAccount("My Checking")
    Savings = BankAccount("Savings")
    print("\nStarting Balance for each account:")
    print(Checking)
    print(Savings)
    print(divider * 10)
    while True:
        print("\nChoose a transaction:")
        print("1. Deposit")
        print("2. Withdraw")
        print("3. Transfer")
        print("4. Check Balance")
        print("5. Exit")
        choice = input("Enter your choice (1-5): ")
        if choice == '1':
            account_num = input(f"Enter the account number (1 for {Checking.label}, 2 for {Savings.label}): ")
            amount_str = input("Enter the deposit amount: ")
            try:
                amount = float(amount_str)
                if account_num == '1':
                    Checking.deposit(amount)
                elif account_num == '2':
                    Savings.deposit(amount)
                else:
                    print("Invalid account number.")
            except ValueError:
                print("Invalid amount, please enter a number.")
        elif choice == '2':
            account_num = input(f"Enter the account number (1 for {Checking.label}, 2 for {Savings.label}): ")
            amount_str = input("Enter the withdrawal amount: ")
            try:
                amount = float(amount_str)
                if account_num == '1':
                    Checking.withdraw(amount)
                elif account_num == '2':
                    Savings.withdraw(amount)
                else:
                    print("Invalid account number.")
            except ValueError:
                print("Invalid amount, please enter a number.")
        elif choice == '3':
            from_account_num = input(f"Enter the sending account number (1 for {Checking.label}, 2 for {Savings.label}): ")
            to_account_num = input(f"Enter the recieving account number (1 for {Checking.label}, 2 for {Savings.label}): ")
            amount_str = input("Enter the amount you want to transfer: ")
            try:
                amount = float(amount_str)
                if from_account_num == '1' and to_account_num == '2':
                    Checking.transfer(amount, Savings)
                elif from_account_num == '2' and to_account_num == '1':
                    Savings.transfer(amount, Checking)
                elif from_account_num == to_account_num:
                    print("Can't transfer funds to the same account.")
                else:
                    print("Invalid account number.")
            except ValueError:
                print("Invalid amount. please enter a number.")
        elif choice == '4':
            account_num = input(f"Enter the account number (1 for {Checking.label}, 2 for {Savings.label}): ")
            if account_num == '1':
                print(Checking)
            elif account_num == '2':
                print(Savings)
            else:
                print("Invalid account number.")
        elif choice == '5':
            print("Exiting the bank now. Goodbye!")
            break
        else:
            print("Invalid, please enter a number between 1 and 5.")
        print(Checking)
        print(Savings)
        print(divider * 10)

if __name__ == "__main__":
    main()

print(divider * 3)
print("Arthur Belanger")
print("CIS-110 - Program : Assignment #8 ")
print(time.ctime())
    
