class BankAccount:
    def __init__(self, account_number, balance):
        self.__account_number = account_number
        self.__balance = balance

    def deposit(self,amount):
        if amount > 0:
            self.__balance += amount
        else: print("Amount must be a positive integer!")

    def withraw(self, amount):
        if amount > 0 and amount < self.__balance:
            self.__balance -= amount

    def display_account_info(self):
        print(f"Account number: ({self.__account_number}) Balance: P{self.__balance}")

    def __display_balance(self):
        print(f"{self.__balance}")

    def get_account_number(self):
        return self.__account_number
    
    def get_balance(self):
        return self.__balance
    
    def set_balance(self, balance):
        if balance > 0:
            self.__balance = balance
        else: print("Invalid amount")
        
account1 = BankAccount(10000, 200)
account1.deposit(100)
account1.withraw(200)
account1.set_balance(-1)
account1.display_account_info()