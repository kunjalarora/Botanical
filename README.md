WELCOME TO BOTANICAL GARDEN.
This project involves all functions related to Garden setup and maintenance.

Developer: Kunjal Arora, Class XII-A

INTRODUCTION

login.py is the login authorisation program.(Managers and Employees can login by providing id and passwords provided.)
user defined modules are - 
  1) manager_propmt.py , 
  2) sales_prompt.py , 
  3) Plants_propmt.py ,
  4) Customer_prompt.py, 
  5) sales_prompt.py.and
  6) reports.py

SOFTWARES
1) MYSQL
2) PYTHON
3) TKINTER

PROCEDURE
 Steps to guide you though my codes execution:-

1. Run the login.py file using python shell. 
    Enter the id and password as per your designation. 
    if you are a manager, enter the id "manager01" with password "OnlyManage01". It will directly take the control to step 2. 
    if you are an employee, enter the id as an integer (valid employee id would be allowed from employee table. Please use password "OnlySell01" . The control will pass onto Step 4, 5 or 6. 

  if you choose to iterate the plants table , refer to step 5. 
  if you choose to iterate the customers table , refer to step 4. 
  if you choose to access the SALES FILE , refer to step 6. 


2. This step is run through file manager_prompt.py. The control is automatically transferred from step 1 using manager's id and password.

    This module allows the manager to perform following operations on employee table in the botanical_garden database using mysql.connector and also allows to fetch reports. 
    Options are-   
         1. Add a new employee 
         2. Update employee data  
         3. Remove an employee 
         4. Retrieve an employee data 
         5. Reports
         6. Quit
		 
		 
3. Reports.py - option 5 in the manager_prompt module (manager_prompt.py) automatically transfers the control to reports module (reports.py file). 
  Here, a tkinter screen will appear. You can click on the three buttons to view the data offered.
  The options provided on the buttons are -
         1. Fetch count of employees joined this month 
         2. Fetch sales count of this month 
         3. Fetch plant inventory

4. customer_prompt.py - This step provides the mainteance operations for customers

5. Plants_prompt.py - This step provides the maintenance operations for plants.  

6. sales_prompt.py - This step accepts the values for executing the sales operation. It refers various other tables and also writes account transaction data to transactions.csv file. 



 
