from tkinter import *  
import sqlite3
import datetime

def clicked():  
    conn = sqlite3.connect('My_finance_journal.db')
    cur = conn.cursor()
    
    cur.execute("""CREATE TABLE IF NOT EXISTS testatabula(
       id INTEGER PRIMARY KEY AUTOINCREMENT,
       kas_nopirkts TEXT,
       datums DATE,
       cena REAL DEFAULT 0.0,
       alga REAL DEFAULT 0.0);
    """)

    tx = txt.get().strip()
    txxx = txt3.get().strip()

    if not tx and not txxx:
        return

    txx = txt2.get().strip().replace(',', '.')
    try:
        cena = float(txx) if txx else 0.0
    except ValueError:
        cena = 0.0

    try:
        alga = float(txxx.replace(',', '.')) if txxx else 0.0
    except ValueError:
        alga = 0.0

    datms = datetime.datetime.now().strftime("%Y-%m-%d")

    cur.execute('INSERT INTO testatabula(kas_nopirkts, datums, cena, alga) VALUES (?, ?, ?, ?)',
                (tx, datms, cena, alga))

    txt.delete(0, END)    
    txt2.delete(0, END)    
    txt3.delete(0, END)    

    conn.commit()
    conn.close()

def read():  
    conn = sqlite3.connect('My_finance_journal.db')
    cur = conn.cursor()
    cur.execute('SELECT kas_nopirkts, cena, datums, alga, id FROM testatabula;')
    all_results = cur.fetchall()
    
    T.delete('1.0', END)
    total_spent = 0.0
    total_income = 0.0

    for entry in all_results:
        try:
            action_id = str(entry[4])
            item_name = entry[0] if entry[0] else "Unknown"
            price = float(entry[1]) if entry[1] not in [None, ""] else 0.0
            date = entry[2] if entry[2] else "Unknown"
            salary = float(entry[3]) if entry[3] not in [None, ""] else 0.0

            total_spent += price
            total_spent = round(total_spent, 2)

            if salary > 0:
                T.insert(INSERT, f"\n\n\t\tSalary >> {date} >> {salary:.2f} €\n")
                total_income += salary
            else:
                T.insert(INSERT, f"\n\tPurchase >> {date} >> {item_name} \n\t\t>> {price:.2f} €")

        except (ValueError, TypeError) as e:
            print(f"Error reading entry: {e}")

    lbbl.configure(text=f'Payed overall: {total_spent:.2f} €')

    # Calculate available balance
    available_balance = round(total_income - total_spent, 2)
    ostatok.configure(text=f'Income: {total_income:.2f} €\n\nAvailable balance: {available_balance:.2f} €')

    conn.commit()
    conn.close()

def close_program():
    window.destroy()

# Create main window
window = Tk()  
window.title("Income and Expense Tracker")
window.geometry('900x700')

Label(window, text="Purchased", font=("Arial Bold", 10)).grid(column=1, row=0) 
Label(window, text="Price (€)", font=("Arial Bold", 10)).grid(column=2, row=0) 
Label(window, text="Salary (€)", font=("Arial Bold", 10)).grid(column=3, row=0) 

lbbl = Label(window, text="Total Spent", font=("Arial Bold", 8))
lbbl.grid(column=2, row=4) 

lbbbl = Label(window, text="Purchase list:", font=("Arial Bold", 10))
lbbbl.grid(column=1, row=7)

dtm = Label(window, text=datetime.datetime.now().strftime("%Y-%m-%d"), font=("Arial Bold", 10))
dtm.grid(column=3, row=3)

ostatok = Label(window, text="Available balance", font=("Arial Bold", 10))
ostatok.grid(column=3, row=7) 

T = Text(window, height=35, width=62, padx=15)
T.grid(column=1, row=8)

Button(window, text="Add to database", command=clicked, width=20).grid(column=1, row=2)
Button(window, text="Read from database", command=read, width=20).grid(column=1, row=4)
Button(window, text="Close", command=close_program, width=20).grid(column=1, row=5)

txt = Entry(window, width=84)
txt.grid(column=1, row=1)

txt2 = Entry(window, width=24)
txt2.grid(column=2, row=1)

txt3 = Entry(window, width=24)
txt3.grid(column=3, row=1)

window.mainloop()

