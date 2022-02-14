import mysql.connector
from datetime import date
def sell(emp_id):
  cnx = mysql.connector.connect(user='root', password='peoplelife@01',
                              host='127.0.0.1',
                              database='botanical_garden')
  cursor_insert = cnx.cursor()
  cursor_select = cnx.cursor(buffered=True)
  cursor_select_all = cnx.cursor()
  cursor_update = cnx.cursor()
  insert_sales = ("INSERT INTO sales_transaction "
               "(transaction_ID,plant_ID,customer_ID,employee_ID, quantity_sold, amount_received,transaction_date) "
               "VALUES (%s, %s, %s, %s, %s, %s, %s)")
  			   
  update_plants = ("UPDATE plants SET quantity_in_stock = %s "
               "WHERE plant_type_ID = %s")

  select_plants = ("SELECT quantity_in_stock, cost_per_plant FROM plants "
               "WHERE plant_type_ID = %s")
  
  select_plants_all = ("SELECT * FROM plants ")
  
  while(True) :
    try :
        plant_id_option =input("This is a Plant selling function. Please enter Plant ID to be sold Use ID for appropriate plant type  (Lotus , Breadfruit, Cacao, Taro are commonly available plants) Enter all to retrieve complete list . Enter Q to exit \n")
        if (plant_id_option == "all") :
          cursor_select_all.execute(select_plants_all)
          myresult = cursor_select_all.fetchall()
          print("rowcount is " +str(cursor_select_all.rowcount))
          if (cursor_select_all.rowcount <= 0 ):
            print("No Row Found.  ")
            continue
          else:
            for x in myresult:
               print(x)
          cnx.commit()
          continue
        if (plant_id_option =="Q"):
          break
        else:
          if (plant_id_option.isnumeric() == False) :
            print('please enter numeric value ')
            continue
          else:
            plant_id_num = int(plant_id_option)
          customer_id = input("Please enter customer ID : ")
          quantity_required = input("Enter quantity to be sold : ")
          data_plants_select = (plant_id_num,)
          cursor_select.execute(select_plants, data_plants_select)
          if (cursor_select.rowcount <= 0 ):
            print("Select available Plant types. retrieve all plants for clarity  ")
            continue
          else:
            quantity_available,cost_each_plant = cursor_select.fetchone()
          cost_each_plant_num = int(cost_each_plant)
          quantity_available_num = int(quantity_available)
          if (cost_each_plant) == 0 :
            print("There is some issue with plant type or plants table")
            continue
          print(cost_each_plant_num)
          print(quantity_required)
          amount = cost_each_plant_num * int(quantity_required)
          sales_id_num = input("Enter sales ID : ")
          print("Total cost of plants sold : " + str(amount)) 
          get_amount = input("Have you received the amount from the customer()y/n) : ") 
          if (get_amount == "y"):
            todaydate = date.today()
            data_sales = (sales_id_num, plant_id_num,customer_id, emp_id, quantity_required, amount,todaydate)
            cursor_insert.execute(insert_sales,data_sales)
            new_quantity = quantity_available_num - int(quantity_required)
            data_update = (new_quantity, plant_id_option)
            cursor_update.execute(update_plants,data_update)
            cnx.commit()
            outfile = open("transactions.csv","a")
            Line = "SaleAccount1,Debit,"+str(todaydate)+","+str(amount)+"\n"
            outfile.write(Line)
            outfile.close()
          break        
    except ValueError :
      print('numeric value expected')
      continue
  cursor_insert.close()
  cursor_update.close()
  cursor_select_all.close()
  cursor_select.close()
  cnx.close()
