
class Account():

    def __init__(self, account, balance):
        
        self.account = account
        self.balance = balance
        self.transactions = []

    
    def deposit (self, amount):
        
        if amount > 0:
            self.balance += amount
            self.transactions.append(f"Deposit: {amount}")
            print("Deposit successfull.")
        
        else:
            print(f"Ammount of {amount} is not valid. Try Again")

    
    def withdraw (self, amount):
        
        if 0 < amount <= self.balance:
            self.balance -= amount
            self.transactions.append(f"Withdraw: {amount}")
            print("Withdraw successfull.")
        
        else:
            print (f"Ammount of {amount} is not valid. Try Again.")

    
    def get_balance(self):
        
        return print(f"Account balance: {self.balance} USD.")
    
    
    def get_transactions(self):

        return print(f"History of transactions: {self.transactions}")
    
    def __str__(self):
        return f"Account {self.account}"
    


class SavingsAccount(Account):

    def __init__(self, account, balance):
        super().__init__(account, balance)
        self.withdraw_limit = 2
        self.withdraw_count = 0


    def withdraw(self, amount):

        if self.withdraw_count <= self.withdraw_limit:

            if 0 < amount <= self.balance:
                self.balance -= amount
                self.transactions.append(f"Withdraw: {amount}")
                self.withdraw_count += 1
                print("Withdraw successfull.")

            else:
                print (f"Ammount of {amount} is not valid. Try Again.")
        
        else:

            print(f"You have come to the max limit of {self.withdraw_limit} limits this month.")
            print(f"If you want you can set a new limit by selecting the option Set new limit on our menu")
    
    def apply_interest(self):

        self.balance *= 1.0035
        print("Month passed, interest applied.")
    
class CheckingAccount (Account):
    
    def __init__(self, account, balance):
        super().__init__(account, balance)
        self.balance_limit = -5000
        self.score = 0
    
    def withdraw(self, amount):
        
        if amount > 0 and (self.balance - amount) >= self.balance_limit:
            self.balance -= amount
            self.transactions.append(f"Withdraw: {amount}")
            print("Withdraw successfull.")
        
        else:
            print (f"Ammount of {amount} is not valid. Try Again.")

    def credit_increase (self):

        for transaction in self.transactions:
            
            if transaction.startswith("Deposit"):
                _, amount = transaction.split(": ")
                self.score += int(float(amount)) // 500
                print(f"Score atual: {self.score}. Limite agora: {abs(self.balance_limit)}USD. ")

        
        if self.score == 0:

            print(f"Unfortunately you cannot increase your limite.")
        
        else:

            self.balance_limit -= (self.score//200)*1000
    
class Client():

    def __init__(self, name, id_number):

        self.name = name
        self.id_number = id_number
        self.accounts = []
    
    def add_account(self, account):

        self.accounts.append(account)
    
    def get_all_balances(self):

        TotalBalance = 0

        for account in self.accounts:

            print(f"{account} has a balance of {account.balance} USD")
            TotalBalance += account.balance
        
        print(f"You have a total balance of {TotalBalance} USD.")
    
    def get_all_transactions(self):

        for account in self.accounts:

            print(f"Here are the transactions of your {account} account: {account.transactions}")
    
    






                







