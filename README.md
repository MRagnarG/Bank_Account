# Python Bank System (CLI)

This project is a simulation of a command-line bank system, built using Python with a modular and testable architecture. It simulates realistic banking behavior like savings interest, overdraft limits, transaction logging, and credit score mechanics.

## Features

- Create and manage clients with multiple bank accounts
- Two account types: `SavingsAccount` and `CheckingAccount`
- Deposits, withdrawals, and automatic interest calculation
- Credit score system that increases overdraft limit on `CheckingAccount`
- Transaction history tracking
- Input validation and clean CLI menus
- Modular code: UI, logic, and tools separated for clarity

## Project Structure

```
bank_account_mod.py    # All core classes and account logic
bank_tools.py          # Reusable financial helper functions
bank_ui.py             # CLI menu system and input/output functions
main.py                # Entry point that runs the CLI using run_app()
README.md              # Project documentation
```

## Example Usage

In `main.py`:
```python
from bank_ui import run_app

if __name__ == "__main__":
    run_app()
```

This starts the command-line interface where users can:
- Create a client
- Add checking/savings accounts
- Perform transactions
- View balances and transaction history

## Docstrings and Code Quality

All core functions and UI handlers now include proper docstrings following a clear and concise format. This helps with readability, documentation, and future testing.

## Educational Purpose

This project was built as part of a learning journey to:
- Practice OOP and modular Python
- Learn to separate concerns (logic, UI, tools)
- Simulate real-world banking systems
- Build a CLI application from scratch

## Next Steps (Future Ideas)

- Add data persistence with JSON or SQLite
- Export transactions to `.csv` or `.txt` files
- Add terminal command shortcuts for quicker access
- Write unit tests for helper functions and account logic
- Build a simple GUI or web version

## Notes on Development

This project was developed by me with support from AI tools like ChatGPT. All architectural decisions, class designs, and testing logic were reviewed and implemented directly by me. The AI served as a code assistant and reviewer during development.

Estimated contribution:
- 90% of code and logic written and reviewed by me
- 10% support through suggestions, feedback, and bug explanations
