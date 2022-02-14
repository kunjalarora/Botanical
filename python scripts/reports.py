from tkinter import *
from tkinter import ttk
import mysql.connector


def fetch_emps(*args):
  result_summary.set(emp_count)
  result.set(emp_all)
  heading1.set("employee count")
  heading2.set("employee detail")

def fetch_sales(*args):
    result.set(amount_sales)  
    result_summary.set(quantity_sold_sales)
    heading1.set("Number of Plants sold")
    heading2.set("Revenue")

def fetch_plants(*args):
    result.set(plants_all)  
    result_summary.set("")
    heading1.set("")
    heading2.set("plant inventory")


def fetch_reports():
  top = Tk()
  # Code to add widgets will go here...
  top.title("Management Reports ")
  mainframe = ttk.Frame(top, padding="5 5 12 12 ")
  mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
  
  cnx = mysql.connector.connect(user='root', password='peoplelife@01',
                              host='127.0.0.1',
                              database='botanical_garden')
  cursor_emp_select = cnx.cursor()
  cursor_sales_select = cnx.cursor()
  cursor_plants_select = cnx.cursor()
  select_employee = ("SELECT employee_ID,name FROM employee "
               "WHERE MONTH(joiningdate) = MONTH(CURRENT_DATE())")
  
  select_sales = ("SELECT SUM(quantity_sold), SUM(amount_received) FROM sales_transaction "
               "WHERE MONTH(transaction_date) = MONTH(CURRENT_DATE())")
  
  select_plants=("SELECT * FROM plants ")
  
  global emp_all
  cursor_emp_select.execute(select_employee)
  emp_all = cursor_emp_select.fetchall()
  
  global emp_count
  emp_count = cursor_emp_select.rowcount
  
  global quantity_sold_sales
  global amount_sales
  cursor_sales_select.execute(select_sales)
  quantity_sold_sales, amount_sales = cursor_sales_select.fetchone()
  
  global plants_all
  cursor_plants_select.execute(select_plants)
  plants_all = cursor_plants_select.fetchall()
  
  
  global result
  result = StringVar()
  global result_summary
  result_summary = StringVar()
  
  ttk.Button(mainframe,text="Fetch count of employees joined this month ", command=fetch_emps).grid(column=1 , row=1, sticky=NW)
  ttk.Button(mainframe,text="Fetch sales count of this month ", command=fetch_sales).grid(column=1 , row=2, sticky=NW)
  ttk.Button(mainframe,text="Fetch plant inventory", command=fetch_plants).grid(column=1 , row=3, sticky=NW)
  
  global heading1
  global heading2
  heading1 = StringVar()
  heading2 = StringVar()
  
  ttk.Label(mainframe,textvariable=heading1).grid(column=1, row=4,stick=NW)
  ttk.Label(mainframe,textvariable=heading2).grid(column=2, row=4,stick=NW)

  ttk.Label(mainframe, textvariable=result_summary).grid(column=1, row=5, sticky=W)
  ttk.Label(mainframe, textvariable=result).grid(column=2, row=5, sticky=W)
  
  
  for child in mainframe.winfo_children():
    child.grid_configure(padx=5, pady=5)
  
  top.mainloop()
  cursor_emp_select.close()
  cursor_plants_select.close()
  cursor_sales_select.close()
  cnx.close()
  