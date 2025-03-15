# Income and Expense Tracker

This is a simple **Income and Expense Tracker** built using **Python** with **Tkinter** for the GUI and **SQLite3** for database management. The program allows users to add purchases, track income, and calculate the available balance.

## Features
- Add purchases and expenses to a database
- Track income and available balance
- Display a list of all transactions
- Simple and intuitive user interface

## Requirements
- Python 3.x
- Tkinter (built-in with Python)
- SQLite3 (built-in with Python)

## Installation
Clone the repository or download the script:

```sh
https://github.com/yourusername/IncomeExpenseTracker.git
cd IncomeExpenseTracker
```

## Usage
Run the Python script:

```sh
python main.py
```

## How It Works
1. Enter the **Purchased item**, **Price**, and **Salary**.
2. Click the **'Add to database'** button to save the entry.
3. Click **'Read from database'** to view all transactions.
4. The program calculates total expenses, total income, and available balance.

## Database Schema
The program creates an SQLite database named `My_finance_journal.db` with the following table:

```sql
CREATE TABLE IF NOT EXISTS testatabula (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    kas_nopirkts TEXT,
    datums DATE,
    cena REAL,
    alga REAL
);
```

## Screenshots

![bd1](https://github.com/user-attachments/assets/331086cf-b1ba-4990-9504-5112e93af603)

![bd2](https://github.com/user-attachments/assets/054d566d-03d0-481f-b9f2-1b3ebf9a5721)

![bd3](https://github.com/user-attachments/assets/bad728db-44b9-442b-9c8b-60be2e769df1)

![bd4](https://github.com/user-attachments/assets/8fba7888-4ec7-4dbc-a7f9-9d732f6559fc)


## Contributing
Feel free to fork the repository and submit pull requests for improvements or bug fixes.

## License
This project is licensed under the MIT License.

