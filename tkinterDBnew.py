
from tkinter import *  
import sqlite3
import datetime
  
def clicked():  
	conn=sqlite3.connect('My_finance_journal.db')
	cur=conn.cursor()
	cur.execute("""CREATE TABLE IF NOT EXISTS testatabula(
   id INTEGER PRIMARY KEY AUTOINCREMENT,
   kas_nopirkts TEXT,
   datums DATE,
   cena REAL,
   alga REAL);
""")
	tx=txt.get()
	txxx=txt3.get()
	
	if (tx=="" and txxx==""):
	    return
	else:
	    txx=txt2.get()
	tyx=txx.replace(',','.')
	tyxx=txxx.replace(',','.')
	
	dtms=datetime.datetime.now()
	datms=dtms.strftime("%D")
	cur=conn.cursor()
	cur.execute('INSERT INTO testatabula(kas_nopirkts,datums, cena, alga) VALUES(?, ?, ?, ?)', [tx, datms, tyx, tyxx,])
	txt.delete('0', END)	
	txt2.delete('0', END)	
	txt3.delete('0', END)	
	conn.commit()
def read():  
	conn=sqlite3.connect('My_finance_journal.db')
	cur=conn.cursor()
	cur.execute('SELECT kas_nopirkts, cena, datums, alga, id FROM testatabula;')
	all_results=cur.fetchall()
	T.delete('1.0', END)
	a=0
	for i in all_results:
		d=u'i'
		try:
			idd=str(i[4])
			g=str(i[0])
			gg=float(i[1])
			dt=str(i[2])
			a+=gg
			a=round(a, 2)
			x=T.insert(INSERT ,idd+' ' +g +' - ' +str(gg)+' € ')
		except:
			pass
		x=T.insert(INSERT, str(i[4])+' ' + str(i[3])+' '+str(i[2])+'\n')
	lbbl.configure(text='Payed overall\n '+ str(a)+ '€')
	cur.execute("SELECT alga, datums FROM testatabula;")
	all_results = cur.fetchall()
	b=0	
	for i in all_results:
		d=u'i'	
		try:
			b+=i[0]
			dtm=i[1]
		except:
			pass
	bb=b-a
	bb=(round(bb, 2))
	ostatok.configure(text='Income '+str(b)+'\n'+dtm+'\n\nAvailable \n balance \n '+str(bb)+'€')
	conn.commit()
now = datetime.datetime.now()
window = Tk()  
window.title("Income and outcome balance program")
window.geometry('600x700')
lbl = Label(window, text="Purchased", font=("Arial Bold", 10))
lbl.grid(column=1, row=0) 
llbll = Label(window, text="   ", font=("Arial Bold", 10))  
llbll.grid(column=2, row=2) 
llbll = Label(window, text="   ", font=("Arial Bold", 10))  
llbll.grid(column=2, row=2) 
lbll = Label(window, text="Price", font=("Arial Bold", 10))
lbll.grid(column=2, row=0) 
lblll = Label(window, text='Salary', font=("Arial Bold", 10))
lblll.grid(column=3, row=0) 
lbbl = Label(window, text="Incomes", font=("Arial Bold", 8))
lbbl.grid(column=2, row=4) 
lbbbl=Label(window, text="Purchase list:", font=("Arial Bold", 10))
lbbbl.grid(column=1, row=7)
dtm = Label(window, text = now.strftime("%D"), font=("Arial Bold", 10))
dtm.grid(column=3, row=3)
ostatok = Label(window, text="Available \n \nbalance \n ", font=("Arial Bold", 10))
ostatok.grid(column=3, row=7) 
T=Text(height=35, width=32)
T.grid(column=1, row=8)
btn = Button(window, text="Add to database ", command=clicked, width=20)
btn.grid(column=1, row=2)
btn.grid(column=1, row=3)
btn = Button(window, text="Read from database", command=read, width=20)
btn.grid(column=1, row=4)
btn = Button(window, text="Close", command=quit, width=20)
btn.grid(column=1, row=5)
txt=Entry(window, width=14)
txt.grid(column=1, row=1)
txt2=Entry(window, width=14)
txt2.grid(column=2, row=1)
txt3=Entry(window, width=14)
txt3.grid(column=3, row=1)
window.mainloop()