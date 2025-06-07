from bank_account_mod import Client, Account, SavingsAccount, CheckingAccount

def show_main_menu():

    """
    Displays the main menu with available options for the user.
    """

    print("\n")
    print("------------------------------------------")
    print("Your Bank")
    print("------------------------------------------")
    print("1. Register a Client.")
    print("2. Add an account. ")
    print("3. Choose account. ")
    print("4. Show balance of your accounts. ")
    print("5. Show Transactions history from your accounts. ")
    print("6. Exit. ")
    print("\n")

def create_client():

    """
    Prompts the user to input a name and ID to create a new client.

    Returns:
        Client: The newly created Client object.
    """

    while True:
        name = input("Enter client's name: ").capitalize()
        if name.isdigit():
            print("Enter a valid name. Numbers not allowed.")
            continue

        id = input("\nEnter clients ID number (8 digits): ").strip()
        if not len(id) == 8:
            print("\nPlease, enter a valid ID number. ")
            continue
        
        client = Client(str(name), id)
        print("\nClient created successfully. ")
        break

    return client

def add_an_account(client):

    """
    Adds a new account (Savings or Checking) to the given client.

    Args:
        client (Client): The client to which the account will be added.
    """

    if client:
        while True:
            account_id = str(len(client.accounts) + 1).zfill(4)
            print("---------------------")
            print("Account types:")
            print("---------------------")
            print("\n")
            print("1. Savings Account")
            print("2. Checking Account")
            print("3. Exit.")
            print("\n")
            try:
                option = int(input("Choose account type: "))
            except ValueError:
                print("\nInvalid input, please enter a number.")
                continue
            if not option in (1,2,3):
                print("\nEnter a valid option. ")
                continue
            if option == 3:
                break
            start_balance = float(input("Enter start balance: "))
            if start_balance < 0:
                print("\nEnter a valid start balance. ")
                continue
            if option == 1:
                savings = SavingsAccount(account_id, start_balance)
                client.add_account(savings)
            elif option == 2:
                checking = CheckingAccount(account_id, start_balance)
                client.add_account(checking)
            continue
    else:
        print("There are no clients registered.")

def account_actions(client, choice):

    """
    Allows the user to perform actions on a selected account:
    deposit, withdraw, apply interest or credit, view balance, or view transactions.

    Args:
        client (Client): The client who owns the account.
        choice (int): The index of the selected account in the client's account list.
    """

    account = client.accounts[choice - 1]
    is_saving = isinstance(account, SavingsAccount)

    index_list = []
    while True:

        print("\n---------------------")
        print("Available actions:")
        print("---------------------")
        print("1. Deposit")
        print("2. Withdraw")
        if is_saving:
            print("3. Apply Interest")
        else:
            print("3. Increase Credit")
        print("4. Show balance")
        print("5. Show transactions history. ")
        print("6. Exit.\n")
                        
        try:
            choice = int(input("Choose an option: "))
        except ValueError:
            print("Invalid input, please enter a number.")
            continue
                        
        print("\n")

        if  choice == 6:
            break

        elif choice == 1:
            amount = float(input("Enter value to deposit: "))
            account.deposit(amount)
            continue

        elif choice == 2:
            amount = float(input("Enter value to withdraw: "))
            account.withdraw(amount)
            continue

        elif choice == 3:
            if is_saving:
                account.apply_interest()
                continue
            else:
                account.credit_increase()
                continue

        elif choice == 4:
            print(account.get_balance())

        elif choice == 5:
            print(account.get_transactions())

        else:
            print("\nEnter a valid choice. ")

def show_accounts(client):

    """
    Displays a list of accounts belonging to the client and allows the user to select one
    to perform further actions.

    Args:
        client (Client): The client whose accounts will be shown.
    """

    if client:  
        if len(client.get_accounts()) == 0:
            print(f"No available accounts, please, add at least one account. ")
            return
             
        while True:
             
            print("---------------------")
            print("Available accounts:")
            print("---------------------\n")

            index_list = []
            for account in client.accounts:
                i = client.accounts.index(account) + 1
                index_list.append(client.accounts.index(account))
                print(f"{i}. {str(account)}")

            print(f"{i + 1}. Exit\n")
                
            try:
                choice = int(input("Choose account: "))
            except ValueError:
                print("\nInvalid input, please enter a number.")
                continue

            if choice == i + 1:
                index_list = []
                break

            elif (choice - 1) in index_list:
                account_actions(client, choice)           

            else:
                print("\nEnter a valid option.")
                continue
    else:
        print("\nThere are no clients registered. ")

def show_balances(client):

    """
    Displays the balances of all accounts associated with the given client.

    Args:
        client (Client): The client whose balances will be displayed.
    """

    if client:
        client.get_all_balances()
    else:
        print("\nThere are no clients registered.")

def show_transactions(client):

    """
    Displays the transaction history of all accounts belonging to the given client.

    Args:
        client (Client): The client whose transaction history will be displayed.
    """

    if client:
        client.get_all_transactions()
    else:
        print("\nThere are no clients registered.")

def exit_app():

    """
    Prints a goodbye message and exits the program.
    """

    print("Thank you for using our app.")
    exit()

def start_bank_cli():

    """
    Runs the main CLI application loop, handling user interaction and routing to
    menu functions.
    """


    while True:

        show_main_menu()

        try:
            choice =int(input("Please, choose an option: "))
        except ValueError:
                        print("\nInvalid input, please enter a number.")
                        continue
        
        print("\n")

        if choice == 6:
            exit_app()

        elif choice == 1:
            client = create_client()

        elif choice == 2:
            add_an_account(client)

        elif choice == 3:
            show_accounts(client)

        elif choice == 4:
            show_balances(client)
        
        elif choice == 5:
            show_transactions(client)
