# Python ATM Simulation

# Overview of the Project
This project is a **simple command-line ATM (Automated Teller Machine) simulation** built entirely in Python. It mimics the basic functionalities of an ATM, allowing a user to log in with an account number and PIN, check their balance, deposit funds, withdraw funds, and reset their PIN.

The account data is stored in a dictionary, simulating a basic database. The system includes essential features like input validation, insufficient funds checks, a daily withdrawal limit, and limited login attempts for security.

# Features
The ATM simulation offers the following functionalities:

* Secure Login:** Users must provide a valid 10-digit account number and a 4-digit PIN. Only 3 login attempts are allowed before the "card" is retained.
* Check Balance:** Displays the current account holder's name and the available balance, formatted as currency.
* Deposit Funds:** Allows the user to add a positive amount to their balance.
* Withdraw Funds:
    * Checks for Insufficient Funds.
    * Enforces a "maximum withdrawal limit of $1000" per transaction.
    * Validates that the withdrawal amount is positive.
* Reset PIN: Allows the user to set a new 4-digit PIN for their account.
* Input Validation:** Handles `ValueError` for non-numeric input in deposit and withdrawal functions.
*  Exit:Terminates the ATM session gracefully.

# Technologies/Tools Used


| Category | Tool/Technology | Description |
|
| "Programming Language" | Python 3.x | The core language used for all logic and functions. |
| "Environment" | Command Line Interface (CLI) | The program runs directly in the terminal/command prompt. |
| "Data Structure" | Python Dictionary | Used to store account data (`ACCOUNTS`) in memory (in-file persistence only). |
| "Libraries" | `time` module | Used for basic pauses (`time.sleep(1)`) to simulate transaction processing time. |

# Installation and Setup
1.  "Save the Code:" Save the provided Python code into a file named `atm_simulator.py`.
2.  "Open Terminal:" Navigate to the directory where you saved the file using your terminal or command prompt.

# Running the Project
Execute the file using the Python interpreter:

# Instructions for Testing
When the script runs, it will first prompt you for your Account Number and PIN.

# Available Test Accounts

Use the following accounts for testing different scenarios:

Account Number             PIN              Name                   Initial Balance                       Test Scenario
1234567890                1111            Salaar                   "$15,008.75"                       Standard transactions.
1030507090                4444            M. Sai Charan            "$807.50"                    Test Insufficient Funds for large withdrawals.
2468013579                3333            AVR Mayuri               "$1,234,795.67"                  Test withdrawal limit ($1000 max).


# Test Cases


Feature                                          Input / Steps                                         Expected Outcome


Successful Login                          "Account: 1234567890, PIN: 1111"                  Access Granted, Main Menu appears.

Login Failure (PIN)                       "Account: 1234567890, PIN: 0000"                Error: Invalid PIN. Attempts remaining update.

Account Balance                            "Login, then select option 1."                  Displays name and the current balance.

Deposit                                 "Login, select 2, Enter amount: 500.50"         "Balance increases by $500.50, successful message shown."

Withdrawal (Valid)                       "Login, select 3, Enter amount: 500"           "Balance decreases by $500.00, successful message shown."

Withdrawal (Limit Exceeded)           "Login, select 3, Enter amount: 1001"                "Print: ""Withdrawal limit exceeded. Maximum                                                                                                                           withdrawal is $1000."""

Withdrawal (Insufficient Funds)      "Login (e.g., as M. Sai Charan), select 3              Enter amount: 1000""Print: ""Insufficient Funds!                                                                                                            Available: $807.50"""

Reset PIN                                    Login, select 4                                 Enter new PIN: 9876","Print: ""PIN successfully                                                                                                             reset for account..."""

Invalid Input                         "When prompted for an amount, enter abc"           "Print: ""Invalid input. Please enter a valid number."""







