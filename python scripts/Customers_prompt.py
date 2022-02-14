import mysql.connector
def entry():
  cnx = mysql.connector.connect(user='root', password='peoplelife@01',
                              host='127.0.0.1',
                              database='botanical_garden')
  cursor_insert = cnx.cursor()
  cursor_delete = cnx.cursor()
  cursor_update = cnx.cursor()
  cursor_select = cnx.cursor()
  add_customer = ("INSERT INTO customers "
               "(customer_ID ,customer_name, address ,contact_number,quantity_sold) "
               "VALUES (%s, %s, %s, %s ,%s)")
  			   
  update_customer = ("UPDATE customers SET customer_name = %s , address = %s, contact_number = %s , quantity_sold= %s "
               "WHERE customer_ID = %s")

  delete_customer = ("DELETE FROM customers WHERE customer_ID = %s")

  select_customer = ("SELECT * FROM customers "
               "WHERE customer_ID = %s")
  
  while(True) :
    try :
        customer_option =input('''This is a menu for customer functions. Please select appropriate option. \n
	 1. Add a new customer \n
         2. Update customer data \n 
         3. Remove a customer \n
	 4. Retrieve a customer's data \n
         5. Quit \n	
	 Select an option : ''')
        if (customer_option.isnumeric() == False) :
          print("Please ensure numeric value ")
          continue
        customer_optint = int(customer_option)
        if (customer_optint ==1) :
          while(True):
            customer_id = input('Enter customer id : ')
            if (customer_id.isnumeric() == False) :
              print('please enter numeric value ')
              continue
            else:
              customer_id_num = int(customer_id)
              break
          customer_name = input('Enter customer name ')
          customer_address = input("Enter customer address")    
          while(True):
            contact = input('Enter contact number : ')
            if (contact.isnumeric() == False) :
              print('please enter numeric value ')
              continue
            else:
              contact_num = int(contact)
              break
          while(True):
            quantity = input('Enter quantity sold : ')
            if (quantity.isnumeric() == False) :
              print('please enter numeric value ')
              continue
            else:
              quantity_num = int(quantity)
              break
          data_customers = (customer_id_num, customer_name,customer_address,contact_num, quantity_num)
          cursor_insert.execute(add_customer, data_customers)
          cnx.commit()
        elif (customer_optint ==2) :
          while(True):
             customer_id = input('Enter customer id : ')
             if (customer_id.isnumeric() == False) :
               print('please enter numeric value ')
               continue
             else:
               customer_id_num = int(customer_id)
               break
          customer_name = input('Enter new customer name : ')
          customer_address = input('Enter new address : ')
          while(True):
            quantity = input('Enter new quantity sold : ')
            if (quantity.isnumeric() == False) :
              print('please enter numeric value ')
              continue
            else:
              quantity_num = int(quantity)
              break
          while(True):
            contact = input('Enter new contact number : ')
            if (contact.isnumeric() == False) :
              print('please enter numeric value ')
              continue
            else:
              contact_num = int(contact)
              break
          update_data_customer = ( customer_name,customer_address, contact_num, quantity_num,customer_id)
          cursor_update.execute(update_customer, update_data_customer)
          cnx.commit()
        elif (customer_optint ==3) :
          while(True):
            customer_id = input('Enter customer id : ')
            if (customer_id.isnumeric() == False) :
              print('please enter numeric value ')
              continue
            else:
              customer_id_num = int(customer_id)
              break
          delete_data_customer = (customer_id_num,)
          cursor_delete.execute(delete_customer, delete_data_customer)
          cnx.commit()
        elif (customer_optint ==4) :
          while(True):
            customer_id = input('Enter customer id : ')
            if (customer_id.isnumeric() == False) :
              print('please enter numeric value ')
              continue
            else:
              customer_id_num = int(customer_id)
              break  
          select_data_customer = (customer_id_num,)
          cursor_select.execute(select_customer, select_data_customer)
          myresult = cursor_select.fetchall()
          if (myresult == None ) :
            print('no row found')
          else:
            for x in myresult:
              print(x)
          cnx.commit()
        elif (customer_optint ==5) :
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
