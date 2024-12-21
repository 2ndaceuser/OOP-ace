class BankAccount:
    def __init__(self, account_number, balance):
        self.__account_number = account_number  
        self.__balance = balance if balance >= 0 else 0  

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
        else:
            print("Deposit amount must be positive.")

    def withdraw(self, amount):
        if amount > 0:
            if amount <= self.__balance:
                self.__balance -= amount
            else:
                print("Insufficient funds.")
        else:
            print("Withdrawal amount must be positive.")

    def display_account_info(self):
        print(f"Account Number: {self.get_account_number()}")
        print(f"Current Balance: {self.get_balance()}")

    def __display_balance(self):
        print(f"Current Balance: {self.__balance}")

    def get_account_number(self):
        return self.__account_number

    def get_balance(self):
        return self.__balance

    def set_balance(self, balance):
        if balance >= 0:
            self.__balance = balance
        else:
            print("Error: Balance cannot be negative.")

if __name__ == "__main__":
    account = BankAccount("123456789", 1000.0)

    account.display_account_info()

    account.deposit(500.0)
    print("After depositing $500:")
    account.display_account_info()

    account.withdraw(300.0)
    print("After withdrawing $300:")
    account.display_account_info()

    account.set_balance(-50.0) 
    print("Attempting to set balance to -50.0:")
    account.display_account_info()

    account.set_balance(2000.0)
    print("After setting balance to $2000:")
    account.display_account_info()