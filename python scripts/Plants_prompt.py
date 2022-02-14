import mysql.connector
def entry():
  cnx = mysql.connector.connect(user='root', password='peoplelife@01',
                              host='127.0.0.1',
                              database='botanical_garden')
  cursor_insert = cnx.cursor()
  cursor_delete = cnx.cursor()
  cursor_update = cnx.cursor()
  cursor_select = cnx.cursor()
  add_plants = ("INSERT INTO plants "
               "(plant_type_ID , plant_type ,quantity_in_stock ,cost_per_plant) "
               "VALUES (%s, %s, %s, %s)")
  			   
  update_plants = ("UPDATE plants SET plant_type = %s , quantity_in_stock = %s , cost_per_plant= %s "
               "WHERE plant_type_ID = %s")

  delete_plants = ("DELETE FROM plants WHERE plant_type_ID = %s")

  select_plants = ("SELECT * FROM plants "
               "WHERE plant_type_ID = %s")
  
  while(True) :
    try :
        plants_option =input('''This is a menu for employee functions. Please select appropriate option. \n
	 1. Add a new plant \n
         2. Update plant data \n 
         3. Remove a plants \n
	 4. Retrieve a plant's data \n
         5. Quit \n	
	 Select an option : ''')
        if (plants_option.isnumeric() == False) :
          print("Please ensure numeric value ")
          continue
        plants_optint = int(plants_option)
        if (plants_optint ==1) :
          while(True):
            plants_type_id = input('Enter plant id : ')
            if (plants_type_id.isnumeric() == False) :
              print('please enter numeric value ')
              continue
            else:
              plants_type_id_num = int(plants_type_id)
              break
          plants_type_n = input('Enter plant type')
          while(True):
            quantity = input('Enter quantity in stock : ')
            if (quantity.isnumeric() == False) :
              print('please enter numeric value ')
              continue
            else:
              quantity_num = int(quantity)
              break
          while(True):
            cost = input('Enter cost per plant : ')
            if (cost.isnumeric() == False) :
              print('please enter numeric value ')
              continue
            else:
              cost_num = int(cost)
              break
          data_plants = (plants_type_id_num, plants_type_n, quantity_num, cost_num)
          cursor_insert.execute(add_plants, data_plants)
          cnx.commit()
        elif (plants_optint ==2) :
          while(True):
             plant_type_id = input('Enter plant id : ')
             if (plant_type_id.isnumeric() == False) :
               print('please enter numeric value ')
               continue
             else:
               plant_type_id_num = int(plant_type_id)
               break
          plant_type = input('Enter new plant type : ')
          while(True):
            quantity = input('Enter new quantity in stock : ')
            if (quantity.isnumeric() == False) :
              print('please enter numeric value ')
              continue
            else:
              quantity_num = int(quantity)
              break
          while(True):
            cost = input('Enter new cost per plant type : ')
            if (cost.isnumeric() == False) :
              print('please enter numeric value ')
              continue
            else:
              cost_num = int(cost)
              break
          update_data_plants = (plant_type_id, plant_type, quantity_num, cost_num)
          cursor_update.execute(update_plants, update_data_plants)
          cnx.commit()
        elif (plants_optint ==3) :
          while(True):
            plants_id = input('Enter plant type id : ')
            if (plants_id.isnumeric() == False) :
              print('please enter numeric value ')
              continue
            else:
              plants_id_num = int(plants_id)
              break
          delete_data_plants = (plants_id_num,)
          cursor_delete.execute(delete_plants, delete_data_plants)
          cnx.commit()
        elif (plants_optint ==4) :
          while(True):
            plant_id = input('Enter plant type id : ')
            if (plant_id.isnumeric() == False) :
              print('please enter numeric value ')
              continue
            else:
              plant_id_num = int(plant_id)
              break  
          select_data_plants = (plant_id_num,)
          cursor_select.execute(select_plants, select_data_plants)
          myresult = cursor_select.fetchall()
          if (myresult == None ) :
            print('no row found')
          else:
            for x in myresult:
              print(x)
          cnx.commit()
        elif (plants_optint ==5) :
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
