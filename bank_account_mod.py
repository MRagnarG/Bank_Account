from bank_tools import can_withdraw, apply_withdraw, calculate_interest, apply_deposit
class Account():

    """
    Base class named Account that takes a initial account ID, balance and empty transfer list (history).

        
    Features:
        Deposit: Deposit an amount to the accounts balance when it's valid.
        Withdraw: Withdraws an amount from the accounts balance when it's valid.
        Get Balance: Shows updated balance.
        Get Transactions: Shows Transactions history.
        __str__: returns the account followed by its ID.
    
    """

    def __init__(self, account, balance):
        
        self.account = account
        self.balance = balance
        self.transactions = []

    
    def deposit (self, amount):
        
        if amount > 0:
            self.balance, self.transactions = apply_deposit(self.balance, amount, self.transactions)
            print("Deposit successfull.")
        
        else:
            print(f"Ammount of {amount} is not valid. Try Again")

    
    def withdraw (self, amount):
        
        if can_withdraw(self.balance, amount):
            self.balance, self.transactions = apply_withdraw(self.balance, amount, self.transactions)
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
    """
    Class named SavingsAccount that takes all previous functions and initial parameters
    from the base class Account. Adds withdraw_limit and withdraw_count.

        
    Features:
        Deposit: Deposit an amount to the accounts balance when it's valid.
        Withdraw: Withdraws an amount from the accounts balance when it's valid.
        Applies Interest: Simulates an interest applying to the balance.
        Get Balance: Shows updated balance.
        Get Transactions: Shows Transactions history.
        __str__: returns the account followed by its ID.
    
    """

    def __init__(self, account, balance):
        super().__init__(account, balance)
        self.withdraw_limit = 2
        self.withdraw_count = 0


    def withdraw(self, amount):

        if self.withdraw_count <= self.withdraw_limit:

            if can_withdraw(self.balance, amount):
                self.balance, self.transactions = apply_withdraw(self.balance, amount, self.transactions)
                print("Withdraw successfull.")
                self.withdraw_count += 1

            else:
                print (f"Ammount of {amount} is not valid. Try Again.")
        
        else:

            print(f"You have come to the max limit of {self.withdraw_limit} limits this month.")
            print(f"If you want you can set a new limit by selecting the option Set new limit on our menu")
    
    def apply_interest(self):

        self.balance = calculate_interest(self.balance)
        print("One month has passed, interest applied. ")

    def __str__(self):
        return f"Savings Account {self.account}"
    
class CheckingAccount (Account):

    """
    Class named CheckingAccount that takes all previous functions and initial parameters
    from the base class Account. Adds a limit to the balance and a score system.

        
    Features:
        Deposit: Deposit an amount to the accounts balance when it's valid.
        Withdraw: Withdraws an amoount from the accounts balance when it's valid.
        Credit Increase System: Checks for available score and determines possible increase on the credit.
        Get Balance: Shows updated balance.
        Get Transactions: Shows Transactions history.
        __str__: returns the account followed by its ID.
    
    """
    
    def __init__(self, account, balance):
        super().__init__(account, balance)
        self.balance_limit = -5000
        self.score = 0
    
    def withdraw(self, amount):
        
        if amount > 0 and (self.balance - amount) >= self.balance_limit:
            self.balance, self.transactions = apply_withdraw(self.balance, amount, self.transactions)
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
    
    def __str__(self):
        return f"Checking Account {self.account}"
    
class Client():

    """
    Class named client that takes initial parameters like name, id number and creates an empty list with
    the users available accounts.
    
    Features:
        Add an account: Creates an account to the user and adds it to the available accounts list.
        Get all balances: Shows to the user all balances from all availables accounts.
        Get all transactions: the user's transaction history.
    """

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
    
    






                







