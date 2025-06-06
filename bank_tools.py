
def calculate_interest(balance):

    """
    Applies interest to the balance.

    Args:
        Balance (float) that the user has from his account.
    
    Returns:
        The updated Balance(float) with the interest applied.
    """

    balance *= 1.0035
    return balance

def can_withdraw (balance, amount):

    """
    Checks if a withdraw can be done in users account.
    
    Args:
        balance (float): users account balance.
        amount (float): amount that will be withdrawn.
    
    Returns:
        Returns True if the withdrawal is valid, otherwise False.
    """
    
    if 0 < amount <= balance:
        return True
    else:
        return False

def apply_withdraw(balance, amount, transac_list):

    """
    Withdraws an amount from the user's account and records the transaction.
    
    Args:
        balance (float): users account balance.
        amount (float): amount that will be withdrawn.
        transac_list (list): list with all previous transactions.
    
    Returns:
        New account balance and updated transactions list with this withdraw transaction.
    """

    balance -= amount
    transac_list.append(f"Withdraw: {amount}")
    
    return balance, transac_list

def apply_deposit(balance, amount, transac_list):

    """
    Deposits an amount to the user's account and records the transaction.
    
    Args:
        balance (float): users account balance.
        amount (float): amount that will be deposited.
        transac_list (list): list with all previous transactions.
    
    Returns:
        New account balance and updated transactions list with this deposit transaction.
    """

    balance += amount
    transac_list.append(f"Deposit: {amount}")

    return balance, transac_list





