import mysql.connector
from datetime import date
import reports
def manage():
  cnx = mysql.connector.connect(user='root', password='peoplelife@01',
                              host='127.0.0.1',
                              database='botanical_garden')
  cursor_insert = cnx.cursor()
  cursor_delete = cnx.cursor()
  cursor_update = cnx.cursor()
  cursor_select = cnx.cursor()
  add_employee = ("INSERT INTO employee "
               "(employee_ID, name, designation, salary, joiningdate) "
               "VALUES (%s, %s, %s, %s, %s)")
  			   
  update_employee = ("UPDATE employee SET name = %s , designation = %s , salary = %s WHERE employee_ID = %s")

  delete_employee = ("DELETE FROM employee WHERE employee_ID = %s")

  select_employee = ("SELECT * FROM employee WHERE employee_ID = %s")
  
  while(True) :
    try :
        manager_option =input('''This is a menu for management functions. Please select appropriate option. \n
         1. Add a new employee \n
         2. Update employee data \n 
         3. Remove an employee \n
         4. Retrieve an employee data \n
         5. Reports \n
         6. Quit \n	
     Select an option : ''')
        if (manager_option.isnumeric() == False) :
          print("Please ensure numeric value ")
          continue
        manager_optint = int(manager_option)
        if (manager_optint ==1) :
          while(True):
            employee_id = input('Enter employee id : ')
            if (employee_id.isnumeric() == False) :
              print('please enter numeric value ')
              continue
            else:
              employee_id_num = int(employee_id)
              break
          employee_name = input('Enter Employee Name : ')
          employee_designation=input('Enter Employee Designation : ')
          while(True):
            salary = input('Enter Salary : ')
            if (salary.isnumeric() == False) :
              print('please enter numeric value ')
              continue
            else:
              salary_num = int(salary)
              break
          todaydate = date.today()
          data_employee = (employee_id_num, employee_name, employee_designation, salary_num, todaydate)
          cursor_insert.execute(add_employee, data_employee)
          cnx.commit()
        elif (manager_optint ==2) :
          while(True):
             employee_id = input('Enter employee id : ')
             if (employee_id.isnumeric() == False) :
               print('please enter numeric value ')
               continue
             else:
               employee_id_num = int(employee_id)
               break
          employee_name = input('Enter new Employee Name : ')
          employee_designation = input('Enter new Employee Designation : ')
          while(True):
            salary = input('Enter new Salary : ')
            if (salary.isnumeric() == False) :
              print('please enter numeric value ')
              continue
            else:
              salary_num = int(salary)
              break
          update_data_employee = (employee_name, employee_designation, salary_num, employee_id_num)
          cursor_update.execute(update_employee, update_data_employee)
          if (cursor_update.rowcount <= 0 ):
            print("No Such Employee.  ")
            continue
          else:
            cnx.commit()
        elif (manager_optint ==3) :
          while(True):
            employee_id = input('Enter employee id : ')
            if (employee_id.isnumeric() == False) :
              print('please enter numeric value ')
              continue
            else:
              employee_id_num = int(employee_id)
              break
          delete_data_employee = (employee_id_num,)
          cursor_delete.execute(delete_employee, delete_data_employee)
          if (cursor_delete.rowcount <= 0 ):
            print("No Such Employee.  ")
            continue
          else:
            cnx.commit()
        elif (manager_optint ==4) :
          while(True):
            employee_id = input('Enter employee id : ')
            if (employee_id.isnumeric() == False) :
              print('please enter numeric value ')
              continue
            else:
              employee_id_num = int(employee_id)
              break  
          select_data_employee = (employee_id_num,)
          cursor_select.execute(select_employee, select_data_employee)
          myresult = cursor_select.fetchall()
          if (myresult == None):
            print("No Such Employee. ")
            continue
          else:
            for x in myresult:
              print(x)
            cnx.commit()
        elif (manager_optint ==5) :
          reports.fetch_reports()
        elif (manager_optint ==6) :
          cursor_insert.close()
          cursor_select.close()
          cursor_update.close()
          cursor_delete.close()
          cnx.close()
          break
        else :
          continue
    except ValueError :
      print('numeric value expected')
      continue
  cursor_insert.close()
  cursor_update.close()
  cursor_delete.close()
  cursor_select.close()
  cnx.close()	
