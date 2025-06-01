# Python Bank System

This project is a simulation of a simple bank system, built using Python and object-oriented programming principles. It includes realistic business rules like savings account interest, overdraft limits, transaction history, and a credit score system that influences the user's available overdraft.

## Features

- Open and manage accounts (`SavingsAccount`, `CheckingAccount`)
- Deposit and withdraw funds with input validation
- Transaction history tracking
- Monthly interest applied to savings accounts
- Credit score increases based on deposit behavior
- Automatic overdraft limit increase based on credit score
- A single client can have multiple accounts (composition)

## Class Structure

- `Account`: Base class containing balance management, deposit, withdraw, and transaction log.
- `SavingsAccount`: Inherits from `Account`, includes withdrawal limits and interest calculation.
- `CheckingAccount`: Inherits from `Account`, allows overdraft and includes a credit score system that can increase the overdraft limit.
- `Client`: Represents a customer who can hold multiple bank accounts.

## Example Usage

```python
client = Client("Ana", "12345678900")
checking = CheckingAccount("0001", 1000)
savings = SavingsAccount("0002", 5000)

client.add_account(checking)
client.add_account(savings)

checking.deposit(1000)
checking.withdraw(400)

savings.apply_interest()

client.get_all_balances()
client.get_all_transactions()
```

## Educational Purpose

This project was developed as part of my Python learning journey, with the goal of improving my understanding of:

- Object-oriented programming
- Modeling real-world systems
- Clean and Pythonic code organization

## File Structure

```
bank_account.py    # Main code with class definitions
README.md          # Project description and usage instructions
```

## Next Steps (future improvements)

- Add JSON-based data persistence (saving/loading accounts)
- Implement terminal menu interface
- Add automated tests using `unittest` or `pytest`
- Build a simple graphical interface with `tkinter` or `PyQt`
