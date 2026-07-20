class BankAccount:
    def __init__(self, acc_no, name, balance=0):
        self.acc_no = acc_no
        self.name = name
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print("Amount Deposited Successfully.")

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            print("Amount Withdrawn Successfully.")
        else:
            print("Insufficient Balance.")

    def check_balance(self):
        print("Current Balance:", self.balance)

    def display(self):
        print("\n----- Account Details -----")
        print("Account Number :", self.acc_no)
        print("Account Holder :", self.name)
        print("Balance        :", self.balance)


class Bank:
    def __init__(self):
        self.accounts = {}

    def create_account(self):
        acc_no = input("Enter Account Number: ")

        if acc_no in self.accounts:
            print("Account already exists.")
            return

        name = input("Enter Account Holder Name: ")
        balance = float(input("Enter Initial Deposit: "))

        self.accounts[acc_no] = BankAccount(acc_no, name, balance)

        print("Account Created Successfully.")

    def deposit(self):
        acc_no = input("Enter Account Number: ")

        if acc_no in self.accounts:
            amount = float(input("Enter Amount: "))
            self.accounts[acc_no].deposit(amount)
        else:
            print("Account Not Found.")

    def withdraw(self):
        acc_no = input("Enter Account Number: ")

        if acc_no in self.accounts:
            amount = float(input("Enter Amount: "))
            self.accounts[acc_no].withdraw(amount)
        else:
            print("Account Not Found.")

    def balance(self):
        acc_no = input("Enter Account Number: ")

        if acc_no in self.accounts:
            self.accounts[acc_no].check_balance()
        else:
            print("Account Not Found.")

    def display(self):
        acc_no = input("Enter Account Number: ")

        if acc_no in self.accounts:
            self.accounts[acc_no].display()
        else:
            print("Account Not Found.")


bank = Bank()

while True:
    print("\n===== BANK MANAGEMENT SYSTEM =====")
    print("1. Create Account")
    print("2. Deposit")
    print("3. Withdraw")
    print("4. Check Balance")
    print("5. Display Account")
    print("6. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        bank.create_account()

    elif choice == 2:
        bank.deposit()

    elif choice == 3:
        bank.withdraw()

    elif choice == 4:
        bank.balance()

    elif choice == 5:
        bank.display()

    elif choice == 6:
        print("Thank You!")
        break

    else:
        print("Invalid Choice.")
