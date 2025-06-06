# Python Bank System

This project is a simulation of a simple bank system, built using Python and object-oriented programming principles. It includes realistic business rules like savings account interest, overdraft limits, transaction history, and a credit score system that influences the user's available overdraft.

## Features

- Open and manage accounts (`SavingsAccount`, `CheckingAccount`)
- Deposit and withdraw funds with input validation
- Transaction history tracking
- Monthly interest applied to savings accounts
- Credit score system that increases based on deposit amounts
- Automatic overdraft limit increase based on credit score
- A single client can have multiple accounts (composition)
- Business logic refactored into reusable helper functions via `bank_tools.py`

## Class Structure

- `Account`: Base class containing balance management, deposit, withdraw, and transaction log.
- `SavingsAccount`: Inherits from `Account`, includes withdrawal limits and interest calculation.
- `CheckingAccount`: Inherits from `Account`, allows overdraft and includes a credit score system that can increase the overdraft limit.
- `Client`: Represents a customer who can hold multiple bank accounts.

These classes delegate financial logic to reusable helper functions for better modularity and testing.

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
bank_account_mod.py    # Contains all class definitions and core account logic
bank_tools.py          # Pure helper functions (e.g. interest, withdraw logic)
README.md              # Project documentation
main.py                # (Planned) Main program with usage demos and test scenarios
```

## Next Steps (future improvements)

- Add JSON-based data persistence (saving/loading accounts).
- Implement terminal menu interface.
- Add automated tests.
- Build a simple graphical interface.
- Create `main.py` as a clean demo/testing entry point using `if __name__ == "__main__":`

## Notes on Development

This project was developed by me as part of my learning process in Python, with support from AI tools like ChatGPT. All design decisions, testing, and code understanding were reviewed and controlled by me.

The AI acted as a coding assistant — similar to how one might use documentation, tutorials, or Stack Overflow — helping with:
- Refining syntax and logic
- Debugging edge cases
- Providing examples and explanations when needed

Estimated contribution:  
- 90% of code written directly by me  
- 10% suggestions, reviews, or improvements guided by AI assistance
